from views.players_view import PlayersView
from models.players import Players
import os


class PlayerController:
    @classmethod
    def list(cls, store, route_params):
        choice = PlayersView.players_view(store["players"])

        if choice == "1":
            return "new_player", None
        elif choice == "2":
            return "delete_player", None
        elif choice == "3":
            return "edit_player", None
        elif choice == "4":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit", None

    @classmethod
    def new_player_controller(cls, store, route_params):
        params = PlayersView.new_player()
        store["players"].append(
            Players(
                params["nom"],
                params["prénom"],
                params["date de naissance"],
                params["sexe"],
                params["rang"],
                params["score"],
            )
        )
        return "players", store

    @classmethod
    def del_player_controller(cls, store, route_params):
        index = PlayersView.del_player_view(store["players"])
        store["players"].pop(int(index) - 1)
        return "players", store

    @classmethod
    def edit_player_controller(cls, store, route_params):
        choice = PlayersView.edit_list_player_view(store["players"])
        choice = int(choice) - 1

        # On efface la console pour avoir une interface propre
        os.system("cls")

        second_choice = PlayersView.edit_player_view(store["players"][choice])
        if second_choice.lower() == "n":
            store["players"][choice].name = input(
                "Taper le nom de fammille du joueur\n"
            )
        elif second_choice.lower() == "p":
            store["players"][choice].first_name = input(
                "Taper le prénom du joueur\n"
            )
        elif second_choice.lower() == "d":
            store["players"][choice].date_of_birth = input(
                "Taper date de naissace du joueur\n"
            )
        elif second_choice.lower() == "s":
            store["players"][choice].sexe = input(
                "Taper M ou F pour déteriner le sexe du joueur\n"
            )
        elif second_choice.lower() == "r":
            store["players"][choice].ranking = input(
                "Taper le rang du joueur\n"
            )

        store["players"][choice].score = 0
        return "players", store
