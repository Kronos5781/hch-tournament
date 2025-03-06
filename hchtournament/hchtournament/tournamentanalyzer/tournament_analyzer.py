from .tournament_analyzer_base import TournamentAnalyzerBase


class TournamentAnalyzer(TournamentAnalyzerBase):

    def __init__(self):
        super().__init__()

    def analyze(self, fp_tournament: str) -> None:

        tournament = self._my_tournament_parser.parse(fp_tournament)
        self._parse_teams(tournament)
        self._parse_categories(tournament)
        self._parse_playling_fields(tournament)
        self._analyze_games(tournament)
