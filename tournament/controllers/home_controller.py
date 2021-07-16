from tournament.views.home_view import HomeView
from tournament.views.players_view import PlayersView

class HomePageController:

    @classmethod
    def dispatch(cls,store, route_params):
        PlayersView.list_player_view(store['players'])
        choice = HomeView.home()
        if choice.lower() == "q":
            next = "quit"
        elif choice == "1":
            next = "new_tournament"
        elif choice == "2":
            next = "players"
        elif choice == "3":
            next = "list_tournament"
        return next , None