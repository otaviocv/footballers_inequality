import psycopg2
from time import sleep
import requests
from bs4 import BeautifulSoup

from league_crawler import *

headers = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

base_url = 'https://www.transfermarkt.co.uk'

def main():
    while True:
        cursor.execute("SELECT * FROM catalog WHERE status = 'new'")
        row = cursor.fetchone()
        if row == None:
            print("All urls already crawled! Get some coffee!")
            continue
        print(row)
        id, url, date_added, date_updated, status, page_type = row
        get_results(url, page_type)
        #try:
            #get_results(url, page_type)
        #except:
            #print(F'Failing: {url}')
            #cursor.execute(F"UPDATE catalog SET status = 'error' WHERE url = '{url}'")
        conn.commit()
        sleep(5)


def get_results(url, page_type):
    if page_type == 'area':
        get_area_results(url)
    elif page_type == 'league':
        get_league_results(url)
    elif page_type == 'team':
        get_team_results(url)
    elif page_type == 'player':
        get_player_results(url)

def get_area_results(url):
    rows = content_list(url)
    for r in rows:
        info_dict = collect_league_info(r)
        league_query = """
INSERT INTO leagues (league, country, clubs, players, avg_age, foreing_players, total_market_value)
VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')
""" % (
    info_dict['league'],
    info_dict['country'],
    info_dict['clubs'],
    info_dict['players'],
    info_dict['avg_age'],
    info_dict['foreing_players'],
    info_dict['total_market_value'],
)
        catalog_query = """
INSERT INTO catalog (url, date_added, status, , page_type)
VALUES ('%s', CURRENT_TIMESTAMP(0), 'new', 'league')
""" % (base_url + info_dict['url'])
        cursor.execute(league_query)
        cursor.execute(catalog_query)
        cursons.commit()
    

def get_league_results(url):
    pass

def get_team_results(url):
    pass

def get_player_results(url):
    pass

def content_list(url):
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.content, 'html5lib')
    table = soup.find(name='table', attrs={'class': 'items'})
    table_body = table.find(name='tbody')
    rows = table_body.findAll('tr', attrs={'class': ['odd', 'even']})
    return rows
def collect_league_info(r): return { 'league': get_league_name(r), 'url': get_league_url(r), 'country': get_country(r), 'clubs': get_clubs_number(r), 'players': get_players_number(r), 'avg_age': get_avg_age(r), 'foreing_players': get_foreign_players_percentage(r), 'total_market_value': get_total_value(r), }


if __name__ == '__main__':
    conn = psycopg2.connect(user='docker',
                            password='docker',
                            host='localhost',
                            port=5555)
    cursor = conn.cursor()
    main()
