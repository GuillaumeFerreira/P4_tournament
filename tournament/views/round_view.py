from views.players_view import PlayersView
class RoundView:
    @classmethod
    def round_view(cls,players,nb_round):
        print("Round n°" + str(nb_round))
        PlayersView.list_player_score_view(players)
