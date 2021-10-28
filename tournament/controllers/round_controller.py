from views.round_view import RoundView
from views.match_view import MatchView
from views.players_view import PlayersView
from models.round import Round
from models.match import Match


class RoundController:
    @classmethod
    def first_round(cls, store, tournament):
        RoundView.round_view(len(tournament.rounds) + 1)
        PlayersView.list_player_score_view(tournament.players)
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

            players_score = {}
            for player in store.data["players"]:
                players_score[player.name] = 0

            if len(tournament.rounds) != 0:
                for round in tournament.rounds:
                    for match in round.matchs:
                        if match.winner is not None:
                            players_score[store.search_player(match.winner).name] = players_score[store.search_player(
                                match.winner).name] + 1

            for player in tournament.players:
                player.score = players_score[player.name]

            list_player_match = tournament.next_round()

        RoundView.round_view(len(tournament.rounds) + 1)



        PlayersView.list_player_score_view(players_score)

        round = Round([])
        for i in range(0, 8, 2):
            round.matchs.append(Match(list_player_match[i], list_player_match[i + 1]))

        for i,round_view in enumerate(tournament.rounds):
            MatchView.match_list_historique(round_view.matchs,i)

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


