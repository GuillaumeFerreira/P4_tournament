class TournamentView:

    @classmethod
    def tournament_view(cls):

        print("1. Modifier les parametres du tournoi\n")
        print("2. Lancer le tournoi\n")
        print("Q. Quitter le programme\n")

        return input("Votre choix: ")

    @classmethod
    def new_tournament_view(cls):
        print("Nouveau tournoi\n")
        name = input("Taper le nom du tournoi : \n")
        place = input("Taper le nom de la ville du tournoi : \n")
        #days = input("Taper le nombre de jour que va durée le tournoi : \n")
        players = ""
        description = input("Taper la description du tournoi : \n")
        time_type = ""

        return name,place,players,description,time_type