from league_crawler import get_all_leagues
from team_crawler import get_all_teams

def main():
    print('Leagues!')
    leagues = get_all_leagues()
    leagues.to_csv('leagues.csv')
    print()
    print('Teams!')
    teams = get_all_teams(leagues.loc[:, ['league', 'url']].values)
    teams.to_csv('teams.csv')
    print('Leagues!')


if __name__ == '__main__':
    main()
