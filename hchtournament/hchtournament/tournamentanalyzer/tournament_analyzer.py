from .tournament_analyzer_base import TournamentAnalyzerBase


class TournamentAnalyzer(TournamentAnalyzerBase):

    def __init__(self):
        super().__init__()

    def analyze(self, fp_tournament: str) -> None:
        pass