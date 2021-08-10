from views.round_view import RoundView
from views.match_view import MatchView
from models.round import Round


class RoundController:
    @classmethod
    def first_round_tournament_save(cls, store, route_params):
        # afficher la liste des tournois et choisir un tournoi à lancer
        RoundView.round_view(store["tournaments"][choice].players)

    @classmethod
    def first_round(cls, store, tournament):
        RoundView.round_view(tournament.players, len(tournament.rounds) + 1)
        round = Round()
        round.init_round(tournament.players)
        MatchView.match_list(round.matchs)

        MatchView.winner_match(round.matchs)

        tournament.rounds.append(round)

        return "next_round", tournament

    @classmethod
    def next_round(cls, store, tournament):
        if len(tournament.rounds) == 4:
            return "end_page", tournament
        else:
            RoundView.round_view(tournament.players, len(tournament.rounds) + 1)
            round = Round()
            round.next_round(tournament.players)
            MatchView.match_list(round.matchs)

            MatchView.winner_match(round.matchs)

            tournament.rounds.append(round)
        return "next_round", tournament
