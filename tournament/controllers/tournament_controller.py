from models.tournament import Tournament
from models.store import Store
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
    def tournament_params(cls, store, tournament):

        field, value = TournamentView.tournament_edit_view(tournament)
        if field == "q":
            return "quit", None
        elif field == "h":
            return "homepage", None
        elif field == "c":
            return "detail_tournament", store.data["tournaments"][choice]
        else:
            setattr(store.data["tournaments"][choice], field, value)

        return "list_tournament", store

    @classmethod
    def new_tournament(cls, store, route_params):
        new_tournament_dic = TournamentView.new_tournament_view()

        new_tournament = Tournament(
            new_tournament_dic["name"],
            new_tournament_dic["place"],
            new_tournament_dic["description"],
            new_tournament_dic["time_type"],
        )
        store.data["tournaments"].append(new_tournament)
        # On efface la console pour avoir une interface propre
        os.system("cls")

        return "detail_tournament", new_tournament

    @classmethod
    def list_tournament(cls, store, route_params):
        choice = TournamentView.list_tournament_view(store.data["tournaments"])
        if choice == "1":
            return "homepage", None

    @classmethod
    def tournament_params_edit(cls, store, route_params):
        choice = TournamentView.list_tournament_edit_view(store.data["tournaments"])
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            choice = int(choice) - 1
            field, value = TournamentView.tournament_edit_view(
                store.data["tournaments"][choice]
            )
            if field == "q":
                return "quit", None
            elif field == "h":
                return "homepage", None
            elif field == "c":
                return "detail_tournament", store.data["tournaments"][choice]
            else:
                setattr(store.data["tournaments"][choice], field, value)

            return "list_tournament", store

    @classmethod
    def add_player_tournament(cls, store, tournament):
        # On efface la console pour avoir une interface propre
        os.system("cls")
        choice = PlayersView.list_choice_player_tournament_view(
            store.data["players"], tournament.players
        )
        if choice.lower() == "a":
            tournament.players = store.data["players"]
        else:
            tournament.players.append(store.data["players"][int(choice) - 1])
        return "detail_tournament", tournament

    @classmethod
    def save_json(cls, store, tournament):


        store.save_json(tournament)

        return "homepage", None

    @classmethod
    def rapports(cls, store, route_params):
        choice = TournamentView.menu_rapport()
        liste_choice = ["1", "2", "3", "4", "5", "6", "7"]
        while choice in liste_choice:
            if choice == "1":
                TournamentView.rapport_acteur_alpha(store.data)
            elif choice == "2":
                TournamentView.rapport_acteur_classement(store.data)
            elif choice == "3":
                TournamentView.rapport_players_tournament_alpha(store.data)
            elif choice == "4":
                TournamentView.rapport_players_tournament_classement(store.data)
            elif choice == "5":
                TournamentView.rapport_tournament(store.data)
            elif choice == "6":
                TournamentView.rapport_tournament_round(store.data)
            elif choice == "7":
                TournamentView.rapport_tournament_match(store.data)

            choice = TournamentView.menu_rapport()
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
