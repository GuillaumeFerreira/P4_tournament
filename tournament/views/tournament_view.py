class TournamentView:

    @classmethod
    def tournament_view(cls):
        print("1. Modifier les parametres du tournoi\n")
        print("2. Lancer le tournoi\n")
        print("3. Retour au menu précédent\n")
        print("Q. Quitter le programme\n")

        return input("Votre choix: ")