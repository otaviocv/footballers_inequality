

def insert_into_catalog(conn, cursor, url, status, page_type):
    query = "INSERT INTO catalog (url, date_added, status, page_type) \n" + \
    F"VALUES ('{url}', CURRENT_TIMESTAMP(0), '{status}', '{page_type}')"
    cursor.execute(query)
    conn.commit()

def insert_into_leagues(conn, cursor, league, country, clubs, players, avg_age, 
                        foreing_players, total_market_value):
    query = "INSERT INTO leagues (league, country, clubs, players, avg_age, foreing_players ,total_market_value) \n"
    F"VALUES ({league}, {country}, {clubs}, {players}, {avg_age}, {foreing_players}, {total_market_value})"
    cursor.execute(query)
    conn.commit()