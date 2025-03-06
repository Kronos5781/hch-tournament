#! /usr/bin/env python3

from hchtournament.tournamentanalyzer import TournamentAnalyzer


def main() -> None:
    
    tournament_analyzer = TournamentAnalyzer()
    tournament_analyzer.analyze("data/spieltag.xlsx")


if __name__ == "__main__":
    main()