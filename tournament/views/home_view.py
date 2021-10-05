class HomeView:
    @classmethod
    def home(cls):
        print("Bienvenue sur le menu principal\n")
        print("1. Gestion des joueurs\n")
        print("2. Gestion des tournois\n")
        print("3. Rapports\n")
        print("Q. Quitter le programme\n")

        return input("Votre choix: \n")
