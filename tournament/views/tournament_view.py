class TournamentView:

    @classmethod
    def tournament_view(cls, tournament):
        print("\nParamètres du tournoi\n")
        print("Nom : " + tournament.name)
        print("Ville : " + tournament.place)
        print("Description : " + tournament.description + "\n")

        print("1. Modifier les parametres du tournoi\n")
        print("2. Lancer le tournoi\n")
        print("3. Revenir sur le menu principal\n")
        print("Q. Quitter le programme\n")

        return input("Votre choix: ")

    @classmethod
    def new_tournament_view(cls):
        print("Nouveau tournoi\n")
        new_tournament ={
        'name' : input("Taper le nom du tournoi : \n"),
        'place' : input("Taper le nom de la ville du tournoi : \n"),
        'description' : input("Taper la description du tournoi : \n"),
        'time_type':  ""}

        return new_tournament

    @classmethod
    def list_tournament_view(cls,tournaments):
        for tournament in tournaments:
            print(tournament.name)
        print("1. Revenir sur le menu principal\n")
        return input("Votre choix: ")

    @classmethod
    def tournament_edit_view(cls,tournament):
        print("\nParamètres du tournoi\n")
        print("1 - Nom : " + tournament.name)
        print("2 - Ville : " + tournament.place)
        print("3 - Description : " + tournament.description + "\n")
        input("Choisir le paramètre à modifier ")

        return input("Votre choix: ")