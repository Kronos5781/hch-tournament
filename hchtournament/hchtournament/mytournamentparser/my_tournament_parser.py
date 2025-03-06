import pandas as pd

from .my_tournament_parser_base import MyTournamentParserBase
from ..models import tournament_models


class MyTournamentParser(MyTournamentParserBase):

    def __init__(self):
        super().__init__()

    def parse(self, fp_tournament: str) -> tournament_models.Tournament:
        
        df = pd.read_excel(fp_tournament)
        game_l = []
        for i, row in df.iterrows():

            game = tournament_models.Game(start=row["Start"],
                                          category=row["Category"],
                                          playing_field=row["Playing field"],
                                          team_1=row["Team 1"],
                                          team_2=row["Team 2"])
            game_l.append(game)

        tournament = tournament_models.Tournament(games=game_l)

        return tournament