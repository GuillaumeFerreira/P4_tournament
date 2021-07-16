class PlayersView:

    @classmethod
    def players_view(cls):
        print("1. Ajouter un joueur au tournoi\n")
        print("2. Supprimer un joueur au tournoi\n")
        print("3. Modifier un joueur\n")
        print("Q. Quitter le programme\n")

        return input("Votre choix: ")

    @classmethod
    def new_player(cls):
        name = input("Taper le nom de fammille du joueur")
        first_name = input("Taper le prénom du joueur")
        date_of_birth = input("Taper date de naissace du joueur")
        sexe = input("Taper M ou F pour déteriner le sexe du joueur")
        ranking = input("Taper le rang du joueur")

        return {'nom' : name,'prénom' : first_name,'date de naissance' : date_of_birth,'sexe' : sexe, 'rang' : ranking}