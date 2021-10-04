from views.players_view import PlayersView
from models.players import Players
from models.store import Store
import os


class PlayerController:
    @classmethod
    def list(cls, store, route_params):

        store.read_json()
        choice = PlayersView.players_view(store.data["players"])

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


        store.add_player_bdd(Players(
                params["nom"],
                params["prénom"],
                params["date de naissance"],
                params["sexe"],
                params["rang"],
                0,
            ))
        """
        store["players"].append(
            Players(
                params["nom"],
                params["prénom"],
                params["date de naissance"],
                params["sexe"],
                params["rang"],
                0,
            )
        )"""
        return "players", store

    @classmethod
    def del_player_controller(cls, store, route_params):

        store.read_json()
        index = PlayersView.del_player_view(store.data["players"])

        store.del_player_bdd(store.data["players"][int(index)])

        #store["players"].pop(int(index) - 1)
        return "players", store

    @classmethod
    def edit_player_controller(cls, store, route_params):

        new_store = Store()

        choice = PlayersView.edit_list_player_view(store.data["players"])
        choice = int(choice)

        # On efface la console pour avoir une interface propre
        os.system("cls")

        second_choice = PlayersView.edit_player_view(store.data["players"][choice])
        if second_choice.lower() == "n":
            new_store.update_player_param(store["players"][choice],"name",input(
                "Taper le nom de fammille du joueur\n"
            ))

        elif second_choice.lower() == "p":
            new_store.update_player_param(store.data["players"][choice],"first_name",input(
                "Taper le prénom du joueur\n"
            ))

        elif second_choice.lower() == "d":
            new_store.update_player_param(store.data["players"][choice],"date_of_birth",(
                "Taper date de naissace du joueur\n"
            ))

        elif second_choice.lower() == "s":
            new_store.update_player_param(store.data["players"][choice], "sexe",input(
                "Taper M ou F pour déteriner le sexe du joueur\n"
            ))
        elif second_choice.lower() == "r":

            new_store.update_player_param(store.data["players"][choice], "ranking", input(
                "Taper le rang du joueur\n"
            ))


        return "players", store
