class TournamentView:
    @classmethod
    def tournament_view(cls, tournament):
        print("\nParamètres du tournoi\n")
        print("Nom : " + tournament.name)
        print("Ville : " + tournament.place)
        print("Description : " + tournament.description + "\n")

        print("1. Modifier les parametres du tournoi\n")
        print("2. Ajouter des joueurs au tournoi\n")
        print("3. Supprimer des joueurs au tournoi\n")
        print("4. Lancer le tourno\n")
        print("5. Sauvegarder le tournoi\n")
        print("6. Revenir sur le menu principal\n")
        print("Q. Quitter le programme\n")

        return input("Votre choix: ")

    @classmethod
    def new_tournament_view(cls):
        print("Nouveau tournoi\n")
        new_tournament = {
            "name": input("Taper le nom du tournoi : \n"),
            "place": input("Taper le nom de la ville du tournoi : \n"),
            "description": input("Taper la description du tournoi : \n"),
            "time_type": "",
        }

        return new_tournament

    @classmethod
    def tournament_edit_view(cls, tournament):
        print("\nParamètres du tournoi\n")
        print("1 - Nom : " + tournament.name)
        print("2 - Ville : " + tournament.place)
        print("3 - Description : " + tournament.description + "\n")
        print("4 - Charger le tournoi\n")
        print("H. Revenir sur le menu principal\n")
        print("Q. Quitter le programme\n")

        second_choice = input("Choisir le paramètre à modifier ou une action")
        if second_choice == "1":
            return "name", input("Taper le nom du tournoi")
        elif second_choice == "2":
            return "place", input("Taper le nom de la ville")
        elif second_choice == "3":
            return "description", input("Taper une nouvelle description")
        elif second_choice == "4":
            return "c", None
        elif second_choice.lower() == "h":
            return "h", None
        elif second_choice.lower() == "q":
            return "q", None

    @classmethod
    def list_tournament_edit_view(cls, tournaments):
        print("\nListe des tournois\n")
        i = 1
        for tournament in tournaments:
            print(
                str(i)
                + " - Nom : "
                + tournament.name
                + " | Nombre de Round déjà effectué "
                + str(len(tournament.rounds))
                + "\n"
            )
        print("H. Revenir sur le menu principal\n")
        print("Q. Quitter le programme\n")

        return input("Choisir un tournoi ")
