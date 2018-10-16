from league_crawler import get_all_leagues
from team_crawler import get_all_teams
from player_crawler import get_all_players
import pandas as pd


def main():
    print('Leagues!')
    leagues = get_all_leagues()
    leagues.to_csv('leagues.csv')
    leagues = pd.read_csv('leagues.csv')
    print()

    print('Teams!')
    teams = get_all_teams(leagues.loc[:, ['league_id', 'url']].values)
    teams.to_csv('teams.csv')
    print()

    print('Players!')
    players = get_all_players(teams.loc[:, ['team_id', 'url']].values)
    players.to_csv('players.csv')
    print()


if __name__ == '__main__':
    main()
