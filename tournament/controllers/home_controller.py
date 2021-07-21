from views.home_view import HomeView
from views.players_view import PlayersView
import os

class HomePageController:

    @classmethod
    def dispatch(cls,store, route_params):


        PlayersView.list_player_view(store['players'])
        choice = HomeView.home()
        premier = 1
        next = "quit"
        while choice != "1" and choice.lower() != "q" and choice != "2" and choice != "3":
            if premier > 1:
                # On efface la console pour avoir une interface propre
                os.system('cls')
                choice = HomeView.home()


            if choice.lower() == "q":
                next = "quit"
            elif choice == "1":
                next = "new_tournament"
            elif choice == "2":
                next = "players"
            elif choice == "3":
                next = "list_tournament"
            premier = premier + 1

        return next , None