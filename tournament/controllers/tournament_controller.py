from models.tournament import Tournament
from views.tournament_view import TournamentView
import os

class TournamentController:

    @classmethod
    def tournament(cls,players):
        choice = TournamentView.tournament_view()
        if choice == "1":
            return "tournament_params",None
        elif choice == "2":
            return "run_tournament",None
        elif choice.lower() == "q":
            return "quit",players

    @classmethod
    def new_tournament(cls,players):
        name, place, players, description, time_type =TournamentView.new_tournament_view()

        new_tournament = Tournament(name, place, players, description, time_type)
        # On efface la console pour avoir une interface propre
        os.system('cls')
        new_tournament.get_params()


        return TournamentController.tournament(),players

