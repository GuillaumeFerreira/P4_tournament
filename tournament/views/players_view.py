class PlayersView:

    @classmethod
    def players_view(cls,players):
        PlayersView.list_player_view(players)
        print("1. Ajouter un joueur au tournoi\n")
        print("2. Supprimer un joueur au tournoi\n")
        print("3. Modifier un joueur\n")
        print("4. Revenir sur le menu principal\n")
        print("Q. Quitter le programme\n")

        return input("Votre choix: ")

    @classmethod
    def new_player(cls):
        name = input("Taper le nom de fammille du joueur\n")
        first_name = input("Taper le prénom du joueur\n")
        date_of_birth = input("Taper date de naissace du joueur\n")
        sexe = input("Taper M ou F pour déteriner le sexe du joueur\n")
        ranking = input("Taper le rang du joueur\n")

        return {'nom' : name,'prénom' : first_name,'date de naissance' : date_of_birth,'sexe' : sexe, 'rang' : ranking}


    def del_player_view(cls, players):
        if players:
            print("Taper le numéro du joueur que vous voulez supprimer\n")
            i = 1
        for player in players:
            print("Joueur "+ str(i) + " : "+player.name)
            i = i + 1
        return input("Votre choix: ")

    @classmethod
    def list_player_view(cls, players):
        if players:
            print("Liste des joueurs inscrit au tournoi\n")
            i = 1
        for player in players:
            print("Joueur "+ str(i) + " : "+player.name)
            i = i +1
        print("\n")