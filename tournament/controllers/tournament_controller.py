from tournament.models.tournament import Tournament
from tournament.views.tournament_view import TournamentView
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
        name, place, description, time_type = TournamentView.new_tournament_view()

        new_tournament = Tournament(name, place, description, time_type)
        store['tournaments'].append(new_tournament)
        # On efface la console pour avoir une interface propre
        os.system('cls')



        return "detail_tournament", new_tournament

    @classmethod
    def list_tournament(cls,store, route_params):
        choice = TournamentView.list_tournament_view(store['tournaments'])
        if choice == "1":
            return "homepage", None

