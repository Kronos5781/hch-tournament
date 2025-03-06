import pandas as pd
from pprint import pprint
from io import StringIO

from ..mytournamentparser import MyTournamentParser
from ..models import tournament_models


class TournamentAnalyzerBase:

    def __init__(self):

        self._my_tournament_parser = MyTournamentParser()

    def _parse_teams(self, tournament: tournament_models.Tournament) -> None:

        teams_dict = {}
        for game in tournament.games:

            if game.category not in teams_dict.keys():
                teams_dict[game.category] = []

            if game.team_1 not in teams_dict[game.category]:
                teams_dict[game.category].append(game.team_1)
            if game.team_2 not in teams_dict[game.category]:
                teams_dict[game.category].append(game.team_2)

        team_l = []
        for category, teams in teams_dict.items():
            for team in teams:
                team = tournament_models.Team(name=team, category=category)
                team_l.append(team)

        tournament.teams = team_l
        print(f"got teams: {len(team_l)}")

    def _parse_categories(self, tournament: tournament_models.Tournament) -> None:

        # find unique categories
        unique_categories = []
        for game in tournament.games:
            if game.category not in unique_categories:
                unique_categories.append(game.category)

        # create models
        category_l = []
        for category_str in unique_categories:
            category = tournament_models.Category(name=category_str)
            category_l.append(category)

        tournament.categories = category_l
        print(
            f"got categories: {len(unique_categories)} -> {unique_categories}"
        )

    def _parse_playling_fields(self, tournament: tournament_models.Tournament) -> None:

        # find unique playing fields
        unique_playing_fields = []
        for game in tournament.games:
            if game.playing_field not in unique_playing_fields:
                unique_playing_fields.append(game.playing_field)

        # create models
        playing_field_l = []
        for playing_field_str in unique_playing_fields:
            playing_field = tournament_models.PlayingField(name=playing_field_str)
            playing_field_l.append(playing_field)

        tournament.playing_fields = playing_field_l
        print(
            f"got playing fields: {len(unique_playing_fields)} -> {unique_playing_fields}"
        )

    def _analyze_games(self, tournament: tournament_models.Tournament) -> None:

        # build csv-header
        csv_header = "team;total;"
        for playing_field in tournament.playing_fields:
            csv_header += f"{playing_field.name};"
        csv_header = csv_header[:-1]

        # iterate over categories and games
        for category in tournament.categories:

            games_per_field = {}
            for game in tournament.games:

                # check if game is in category
                if category.name != game.category:
                    continue

                # check if team is in dict
                if game.team_1 not in games_per_field.keys():
                    games_per_field[game.team_1] = {"total": 0}
                if game.team_2 not in games_per_field.keys():
                    games_per_field[game.team_2] = {"total": 0}

                # check if playing field is in team dict
                if game.playing_field not in games_per_field[game.team_1].keys():
                    games_per_field[game.team_1][game.playing_field] = 0
                if game.playing_field not in games_per_field[game.team_2].keys():
                    games_per_field[game.team_2][game.playing_field] = 0

                # increment games
                games_per_field[game.team_1][game.playing_field] += 1
                games_per_field[game.team_2][game.playing_field] += 1
                games_per_field[game.team_1]["total"] += 1
                games_per_field[game.team_2]["total"] += 1

            # build csv data
            csv_data = f"{csv_header}\n"
            for team, fields in games_per_field.items():
                csv_data += f"{team};"
                csv_data += f"{fields['total']};"
                for playing_field in tournament.playing_fields:
                    csv_data += f"{fields.get(playing_field.name, 0)};"
                csv_data = csv_data[:-1]
                csv_data += "\n"

            # print csv
            data = StringIO(csv_data)
            df = pd.read_csv(data, sep=";")
            print("-" * 60)
            print(f"Category: {category.name.upper()}")
            print(df)
            print("-" * 60)

            # write csv
            with open(f"data/{category.name}.csv", "w") as f:
                f.write(csv_data)
