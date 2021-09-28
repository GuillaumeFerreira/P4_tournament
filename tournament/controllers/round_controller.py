from views.round_view import RoundView
from views.match_view import MatchView
from models.round import Round
from models.match import Match


class RoundController:
    @classmethod
    def first_round(cls, store, tournament):
        RoundView.round_view(tournament.players, len(tournament.rounds) + 1)
        round = Round([])
        round.init_round(tournament.players)
        MatchView.match_list(round.matchs)

        save = MatchView.winner_match(round.matchs)

        tournament.rounds.append(round)
        if save.lower() == "s":
            return "save_tournament", tournament
        else:
            return "next_round", tournament

    @classmethod
    def next_round(cls, store, tournament):
        if len(tournament.rounds) == 4:
            return "end_page", tournament
        else:

            list_player_match = tournament.next_round()

        RoundView.round_view(tournament.players, len(tournament.rounds) + 1)
        round = Round([])
        for i in range(0, 8, 2):
            round.matchs.append(
                Match(list_player_match[i], list_player_match[i + 1])
            )

        for round_view in tournament.rounds:
            MatchView.match_list(round_view.matchs)

        MatchView.match_list(round.matchs)

        save = MatchView.winner_match(round.matchs)

        tournament.rounds.append(round)

        if save.lower() == "s":
            return "save_tournament", tournament
        else:
            return "next_round", tournament

    @classmethod
    def end_match(cls, store, tournament):
        RoundView.winner(tournament.players)

        return "quit", None
