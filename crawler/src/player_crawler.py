import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

headers = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

base_url = 'https://www.transfermarkt.co.uk/'
s = requests.Session()
s.headers.update(headers)


def get_all_players(teams_list):
    tables = []
    for team_id, team_url in tqdm(teams_list[365:]):
        url = base_url + team_url[1:]
        table = get_team_table(team_id, url)
        tables.append(table)
    players_table = pd.concat(tables, sort=True) \
                      .drop_duplicates() \
                      .reset_index(drop=True)
    return players_table


def get_team_table(team_id, team_url):
    team_table = get_players(team_url)
    team_table['team_id'] = team_id
    return team_table


def get_players(team_url):
    print(team_url)
    result = s.get(team_url)
    soup = BeautifulSoup(result.content, 'html5lib')
    table = soup.find(name='table', attrs={'class': 'items'})
    if table is None:
        return pd.DataFrame()
    table_body = table.find(name='tbody')
    rows = table_body.findAll('tr', attrs={'class': ['odd', 'even']})
    t = []
    for r in rows:
        t.append({
            'name': get_name(r),
            'number': get_number(r),
            'position': get_position(r),
            'date_of_birth_and_age': get_date_of_birth_and_age(r),
            'nationality': get_nationalities(r),
            'market_value': get_market_value(r)
        })
    return pd.DataFrame(t)


def get_number(row):
    return row.find('div', {'class': 'rn_nummer'}).contents[0]


def get_name(row):
    return row.find('a', {'class': 'spielprofil_tooltip'}).contents[0]


def get_position(row):
    return row.find('table').findAll('td')[2].contents[0]


def get_date_of_birth_and_age(row):
    return row.findAll('td', {'class': 'zentriert'})[1].contents[0]


def get_nationalities(row):
    countries_img = row.findAll('img', {'class': 'flaggenrahmen'})
    nationalities = [x.get('title') for x in countries_img]
    if len(nationalities) == 1:
        return nationalities[0]
    return str(nationalities)


def get_market_value(row):
    return row.find('td', {'class': 'rechts hauptlink'}).contents[0]
