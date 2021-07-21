class HomeView:


    @classmethod
    def home(cls):
        print("Bienvenue sur la gestion du tournoi\n")
        print("1. Créer un tournoi\n")
        print("2. Gestion des joueurs\n")
        print("3. Gestion des tournois\n")
        print("Q. Quitter le programme\n")

        return input("Votre choix: ")
