from views.home_view import HomeView
from views.players_view import PlayersView

class HomePageController:

    @classmethod
    def dispatch(cls,players):
        PlayersView.list_player_view(players)
        choice = HomeView.home()
        if choice.lower() == "q":
            next = "quit"
        elif choice == "1":
            next = "new_tournament"
        elif choice == "2":
            next = "players"
        elif choice == "3":
            next = "save"
        return next ,players