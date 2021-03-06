from views.home_view import HomeView
from views.players_view import PlayersView


class HomePageController:
    @classmethod
    def dispatch(cls, store, route_params):

        PlayersView.list_player_view(store.data["players"])
        choice = HomeView.home()

        if choice.lower() == "q":
            next = "quit"

        elif choice == "1":
            next = "players"
        elif choice == "2":
            next = "list_tournament"
        elif choice == "3":
            next = "rapports"

        return next, None
