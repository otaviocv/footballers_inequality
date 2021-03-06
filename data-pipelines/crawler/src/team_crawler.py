import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import hashlib

headers = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

base_url = 'https://www.transfermarkt.co.uk/'
s = requests.Session()
s.headers.update(headers)


def get_all_teams(leagues_list):
    tables = []
    for league_id, league_url in tqdm(leagues_list):
        url = base_url + league_url[1:]
        table = get_league_table(league_id, url)
        tables.append(table)
    teams_table = pd.concat(tables, sort=True) \
                    .drop_duplicates() \
                    .reset_index(drop=True)
    teams_id = teams_table.apply(lambda x: hashlib.md5((x.league_id +
                                                        x.team).encode())
                                                  .hexdigest(), axis=1)
    teams_table['team_id'] = teams_id
    return teams_table


def get_league_table(league_id, league_url):
    league_table = get_teams(league_url)
    league_table['league_id'] = league_id
    return league_table


def get_teams(league_url):
    print(league_url)
    result = s.get(league_url)
    soup = BeautifulSoup(result.content, 'html5lib')
    print(is_cup(soup))
    if is_cup(soup):
        return pd.DataFrame()
    table = soup.find(name='table', attrs={'class': 'items'})
    if table is None:
        return pd.DataFrame()
    table_body = table.find(name='tbody')
    rows = table_body.findAll('tr', attrs={'class': ['odd', 'even']})
    t = []
    for r in rows:
        t.append({
            'team': get_team_name(r),
            'url': get_team_url(r),
            'players': get_n_of_players(r),
            'foreing_players': get_foreingners(r),
            'avg_age': get_avg_age(r),
            'total_market_value': get_total_market_value(r),
            'avg_market_value': get_avg_market_value(r)
        })
    return pd.DataFrame(t)


def is_cup(soup):
    type_of_cup = soup.find('span', {'class': 'dataItem'})
    return type_of_cup is not None


def get_team_name(row):
    return row.find('img').get("alt")


def get_team_url(row):
    return row.findAll('a')[1].get('href')


def get_n_of_players(row):
    tds = row.findAll('td')
    if len(tds) <= 3:
        return None
    return tds[3].find('a').contents[0]


def get_avg_age(row):
    tds = row.findAll('td')
    if len(tds) <= 4:
        return None
    return tds[4].contents[0]


def get_foreingners(row):
    tds = row.findAll('td')
    if len(tds) <= 5:
        return None
    return tds[5].contents[0]


def get_total_market_value(row):
    tds = row.findAll('td')
    if len(tds) <= 6:
        return None
    return tds[6].find('a').contents[0]


def get_avg_market_value(row):
    tds = row.findAll('td')
    if len(tds) <= 7:
        return None
    return tds[7].contents[0]
