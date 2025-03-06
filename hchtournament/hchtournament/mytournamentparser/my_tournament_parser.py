import pandas as pd

from .my_tournament_parser_base import MyTournamentParserBase
from ..models import tournament_models


class MyTournamentParser(MyTournamentParserBase):

    def __init__(self):
        super().__init__()

    def parse(self, fp_tournament: str) -> tournament_models.Tournament:
        
        df = pd.read_excel(fp_tournament)
        print(df)