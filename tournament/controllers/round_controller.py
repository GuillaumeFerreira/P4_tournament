from views.round_view import RoundView
from views.match_view import MatchView
from models.round import Round
from models.match import Match

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

            players = tournament.next_round(tournament.players)
            for i in range(0,8,2):
                round.matchs.append(Match(players[i], players[i + 1]))

            for round_view in tournament.rounds:
                MatchView.match_list(round_view.matchs)

            MatchView.match_list(round.matchs)

            #for match in round.matchs:
                #tournament.has_played(match.first_player.name,match.second_player.name)

            MatchView.winner_match(round.matchs)

            tournament.rounds.append(round)
        return "next_round", tournament

    @classmethod
    def end_match(cls, store, tournament):
        RoundView.winner(tournament.players)

        return "quit", None
