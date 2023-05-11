from requests import get
from pprint import PrettyPrinter

BASE_URL = "http://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()


def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links


def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']

    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        print("----------------------------------------------------------")
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']} - {away_team['score']}")
        print(f"{clock} - {period['current']}")


get_scoreboard()

#! this portion was directly copied from another source but it did not work at all.MAY BE it's API has been called off!
# def get_stats():
#     stats = get_links()['leagueTeamStatsLeaders']
#     teams = get(
#         BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

#     teams = list(filter(lambda x: x['name'] != "Team", teams))
#     teams.sort(key=lambda x: int(x['ppg']['rank']))

#     for i, team in enumerate(teams):
#         name = team['name']
#         nickname = team['nickname']
#         ppg = team['ppg']['avg']
#         print(f"{i + 1}. {name} - {nickname} - {ppg}")

# get_stats()

# def gets_stats():
#     stats = get_links()['leagueTeamStatsLeaders']
#     teams = get(
#         BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']
#     teams = list(filter(lambda x: x['name'] != "Team", teams))
#     teams.sort(key=lambda x: int(x['ppg']['rank']))

#     for i, team in enumerate(teams):
#         name = team['name']
#         nickname = team['nickname']
#         ppg = team['ppg']['avg']
#         print(f"{i + 1}. {name} - {nickname} - {ppg}")

# ! could not find "leagueTeamStatsLeaders" in the link on the fist attemp. reason: unknown.
# ?HENCE  the out come is postporned!

# gets_stats()

# printer.pprint(get_links())
