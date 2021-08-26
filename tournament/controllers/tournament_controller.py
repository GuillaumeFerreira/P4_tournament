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
        data = {}
        data["tournament"] = tournament.to_dict()
        data["players"] = []
        data["rounds"] = []
        data["matchs"] = []
        for player in tournament.players:

            data["players"].append(player.to_dict())

        for round in tournament.rounds:
            data["rounds"].append(round.to_dict())
            for match in round.matchs:
                data["matchs"].append(match.to_dict())



        with open('save/' + tournament.name + "_data.json", "w") as outfile:
            json.dump(data, outfile)
        return "homepage", None
