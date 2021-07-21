from models.tournament import Tournament
from views.tournament_view import TournamentView
import os

class TournamentController:

    @classmethod
    def detail_tournament(cls,store, tournament):

        choice = TournamentView.tournament_view(tournament)
        if choice == "1":
            return "tournament_params", tournament
        elif choice == "2":
            return "run_tournament", tournament
        elif choice == "3":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit", None

    @classmethod
    def new_tournament(cls, store, route_params):
        new_tournament_dic = TournamentView.new_tournament_view()

        new_tournament = Tournament(new_tournament_dic['name'], new_tournament_dic['place'], new_tournament_dic['description'], new_tournament_dic['time_type'])
        store['tournaments'].append(new_tournament)
        # On efface la console pour avoir une interface propre
        os.system('cls')



        return "detail_tournament", new_tournament

    @classmethod
    def list_tournament(cls,store, route_params):
        choice = TournamentView.list_tournament_view(store['tournaments'])
        if choice == "1":
            return "homepage", None

    @classmethod
    def tournament_params_edit(cls,store, route_params):
        choice = TournamentView.list_tournament_edit_view(store['tournaments'])
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            choice = int(choice) - 1
            second_choice = TournamentView.tournament_edit_view(store['tournaments'][choice])
            if second_choice == "1":
                store['tournaments'][choice].name = input("Taper le nom du tournoi")
            elif second_choice == "2":
                store['tournaments'][choice].place = input("Taper le nom de la ville")
            elif second_choice == "3":
                store['tournaments'][choice].description = input("Taper une nouvelle description")
            elif second_choice.lower() == "h":
                return "homepage", None
            elif second_choice.lower() == "q":
                return "quit", None

            return "list_tournament",store