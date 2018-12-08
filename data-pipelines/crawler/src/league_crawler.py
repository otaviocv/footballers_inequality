import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import hashlib

from utils import convert_market_value

headers = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

def get_all_leagues():
    tables = []
    for region in regions_list:
        url = region_url + region
        print(url)
        table = get_region_table(url)
        tables.append(table)
    league_table = pd.concat(tables) \
                     .drop_duplicates() \
                     .reset_index(drop=True)
    league_ids = league_table.apply(lambda x: hashlib.md5((x.country +
                                                           x.league).encode())
                                                     .hexdigest(), axis=1)
    league_table['league_id'] = league_ids
    return league_table


def get_region_table(url):
    urls = all_pages_url(url)
    tables = [get_page_table(u) for u in tqdm(urls)]
    return pd.concat(tables)


def all_pages_url(url):
    return [url + F'?ajax=yw1&page={u}' for u in range(1, 15)]


def get_page_table(url):
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.content, 'html5lib')
    table = soup.find(name='table', attrs={'class': 'items'})
    table_body = table.find(name='tbody')
    rows = table_body.findAll('tr', attrs={'class': ['odd', 'even']})
    t = []
    for r in rows:
        t.append({
            'league': get_league_name(r),
            'url': get_league_url(r),
            'country': get_country(r),
            'clubs': get_clubs_number(r),
            'players': get_players_number(r),
            'avg_age': get_avg_age(r),
            'foreing_players': get_foreign_players_percentage(r),
            'total_market_value': get_total_value(r),
        })
    return pd.DataFrame(t)


def get_league_name(row):
    r = row.find('img', {'class': ""}).get("alt")
    return r.replace("'", ' ')


def get_league_url(row):
    return row.findAll('a')[1].get('href')


def get_country(row):
    return row.find('img', {'class': 'flaggenrahmen'}).get('alt')


def get_clubs_number(row):
    r = row.findAll('td', {'class': 'zentriert'})[1].contents[0]
    return int(r)


def get_players_number(row):
    r = row.findAll('td', {'class': 'zentriert'})[2].contents[0]
    return int(r.replace('.', ''))


def get_avg_age(row):
    r = row.findAll('td', {'class': 'zentriert'})[3].contents[0]
    return float(r.replace(',', '.'))


def get_foreign_players_percentage(row):
    r = row.findAll('td', {'class': 'zentriert'})[4].find('a').contents[0]
    return float(r.replace(',', '.').replace('%', ''))


def get_total_value(row):
    r = row.find('td', {'class': 'rechts'}).contents[0]
    v = convert_market_value(r)
    print(v)
    return v
