from views.players_view import PlayersView
class RoundView:
    @classmethod
    def round_view(cls,players):
        PlayersView.list_player_score_view(players)
