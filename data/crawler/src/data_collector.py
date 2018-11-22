import psycopg2
from time import sleep

def main():
    while True:
        cursor.execute("SELECT * FROM catalog WHERE status = 'new'")
        row = cursor.fetchone()
        if row == None:
            print("All urls already crawled! Get some coffee!")
            continue
        print(row)
        id, url, date_added, date_updated, status, page_type = row
        try:
            get_results(url, page_type)
        except:
            print(F'Failing: {url}')
            cursor.execute(F"UPDATE catalog SET status = 'error' WHERE url = '{url}'")
        conn.commit()


def get_results(url, page_type):
    if page_type = 'area':
        pass
    elif page_type = 'league':
        pass
    elif page_type = 'team':
        pass
    elif page_type = 'player':
        pass


if __name__ == '__main__':
    conn = psycopg2.connect(user='docker',
                            password='docker',
                            host='localhost',
                            port=5555)
    cursor = conn.cursor()
    main()
