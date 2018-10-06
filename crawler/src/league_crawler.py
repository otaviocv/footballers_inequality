import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from time import sleep

headers = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

base_url = 'https://www.transfermarkt.co.uk/'
region_suffix = 'wettbewerbe/'
region_url = base_url + region_suffix
regions_list = ['amerika', 'europa', 'asien', 'europa', 'afrika']


def get_all_leagues():
    tables = []
    for region in regions_list:
        url = region_url + region
        print(url)
        table = get_region_table(url)
        tables.append(table)
    league_table = pd.concat(tables)
    #league_table.to_csv('leagues.csv')
    return league_table


def get_region_table(url):
    urls = all_pages_url(url)
    tables = [get_page_table(u) for u in tqdm(urls)]
    return pd.concat(tables)


def all_pages_url(url):
    return [url + F'?ajax=yw1&page={u}' for u in range(1, 15)]


def get_page_table(url):
    result = requests.get(url, headers=headers)
    sleep(1)
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
    return row.find('img', {'class': ""}).get("alt")


def get_league_url(row):
    return row.findAll('a')[1].get('href')


def get_country(row):
    return row.find('img', {'class': 'flaggenrahmen'}).get('alt')


def get_clubs_number(row):
    return row.findAll('td', {'class': 'zentriert'})[1].contents[0]


def get_players_number(row):
    return row.findAll('td', {'class': 'zentriert'})[2].contents[0]


def get_avg_age(row):
    return row.findAll('td', {'class': 'zentriert'})[3].contents[0]


def get_foreign_players_percentage(row):
    return row.findAll('td', {'class': 'zentriert'})[4].find('a').contents[0]


def get_total_value(row):
    return row.find('td', {'class': 'rechts'}).contents[0]
