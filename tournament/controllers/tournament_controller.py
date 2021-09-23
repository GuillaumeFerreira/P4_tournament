from models.tournament import Tournament
from views.tournament_view import TournamentView
from views.players_view import PlayersView
import os
import json


class TournamentController:
    @classmethod
    def detail_tournament(cls, store, tournament):

        choice = TournamentView.tournament_view(tournament)
        if choice == "1":
            return "tournament_params", tournament
        if choice == "2":
            return "add_player_tournament", tournament
        if choice == "3":
            return "del_player_tournament", tournament
        elif choice == "4":
            return "first_round", tournament
        elif choice == "5":
            return "save_tournament", tournament
        elif choice == "6":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit", None

    @classmethod
    def new_tournament(cls, store, route_params):
        new_tournament_dic = TournamentView.new_tournament_view()

        new_tournament = Tournament(
            new_tournament_dic["name"],
            new_tournament_dic["place"],
            new_tournament_dic["description"],
            new_tournament_dic["time_type"],
        )
        store["tournaments"].append(new_tournament)
        # On efface la console pour avoir une interface propre
        os.system("cls")

        return "detail_tournament", new_tournament

    @classmethod
    def list_tournament(cls, store, route_params):
        choice = TournamentView.list_tournament_view(store["tournaments"])
        if choice == "1":
            return "homepage", None

    @classmethod
    def tournament_params_edit(cls, store, route_params):
        choice = TournamentView.list_tournament_edit_view(store["tournaments"])
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            choice = int(choice) - 1
            field, value = TournamentView.tournament_edit_view(
                store["tournaments"][choice]
            )
            if field == "q":
                return "quit", None
            elif field == "h":
                return "homepage", None
            elif field == "c":
                return "detail_tournament", store["tournaments"][choice]
            else:
                setattr(store["tournaments"][choice], field, value)

            return "list_tournament", store

    @classmethod
    def add_player_tournament(cls, store, tournament):
        # On efface la console pour avoir une interface propre
        os.system("cls")
        choice = PlayersView.list_choice_player_tournament_view(
            store["players"], tournament.players
        )
        if choice.lower() == "a":
            tournament.players = store["players"]
        else:
            tournament.players.append(store["players"][int(choice) - 1])
        return "detail_tournament", tournament

    @classmethod
    def save_json(cls, store, tournament):
        f = open("save/players_data.json")
        data_load = json.load(f)
        data = {}
        list_id_player = []
        data["players"] = []

        for players in data_load["players"]:
            list_id_player.append(
                {
                    "id": players["id"],
                    "name": players["name"],
                    "first_name": players["first_name"],
                    "date_of_birth": players["date_of_birth"],
                    "type": players["type"],
                    "ranking": players["ranking"],
                    "score": players["score"],
                }
            )
            data["players"].append(players["id"])

        data_players = {}
        data["tournament"] = tournament.to_dict()

        data_players["players"] = list_id_player

        for i, player in enumerate(tournament.players):
            if player.id not in list_id_player[i]["id"]:
                data_players["players"].append(player.to_dict())

        with open("save/" + tournament.name + "_data.json", "w") as outfile:
            json.dump(data, outfile)

        with open("save/players_data.json", "w") as outfile:
            json.dump(data_players, outfile)
        return "homepage", None

    @classmethod
    def rapports(cls, store, route_params):
        choice = TournamentView.menu_rapport()
        liste_choice = ["1", "2", "3", "4", "5", "6", "7"]
        while choice in liste_choice:
            if choice == "1":
                TournamentView.rapport_acteur_alpha(store)
            elif choice == "2":
                TournamentView.rapport_acteur_classement(store)
            elif choice == "3":
                TournamentView.rapport_players_tournament_alpha(store)
            elif choice == "4":
                TournamentView.rapport_players_tournament_classement(store)
            elif choice == "5":
                TournamentView.rapport_tournament(store)
            elif choice == "6":
                TournamentView.rapport_tournament_round(store)
            elif choice == "7":
                TournamentView.rapport_tournament_match(store)

            choice = TournamentView.menu_rapport()
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
