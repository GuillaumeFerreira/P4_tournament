class PlayersView:
    @classmethod
    def players_view(cls, players):
        PlayersView.list_player_view(players)
        print("1. Ajouter un joueur\n")
        print("2. Supprimer un joueur\n")
        print("3. Modifier un joueur\n")
        print("4. Revenir sur le menu principal\n")
        print("Q. Quitter le programme\n")

        return input("Votre choix: \n")

    @classmethod
    def new_player(cls):
        name = input("Taper le nom de fammille du joueur\n")
        first_name = input("Taper le prénom du joueur\n")
        date_of_birth = input("Taper date de naissace du joueur\n")
        sexe = input("Taper M ou F pour déteriner le sexe du joueur\n")
        ranking = input("Taper le rang du joueur\n")

        return {
            "nom": name,
            "prénom": first_name,
            "date de naissance": date_of_birth,
            "sexe": sexe,
            "rang": ranking,
        }

    @classmethod
    def del_player_view(cls, players):
        if players:
            print("Taper le numéro du joueur que vous voulez supprimer\n")

        for i, player in enumerate(players):
            print("Joueur n° " + str(i) + " : " + player.name)

        return input("Votre choix: ")

    @classmethod
    def list_player_view(cls, players):
        if players:
            print("Liste des joueurs\n")

        for i, player in enumerate(players):
            print(
                "Joueur n° "
                + str(i)
                + " : "
                + player.name
                + " | Rang : "
                + str(player.ranking)
            )

        print("\n")

    @classmethod
    def list_choice_player_tournament_view(cls, players, tournament_players):
        print("Liste des joueurs\n")

        for i, player in enumerate(players):
            if player not in tournament_players:
                print("Joueur n° " + str(i) + " : " + player.name)

        print("\n")
        print("Liste des joueurs déjà inscrit au tournoi\n")
        for player in tournament_players:
            print("Joueur  : " + player.name)

        print("\n")

        return input(
            "Ajouter un joueur en entrant son numéro ou"
            ' taper " a " pour les ajouter tous \n'
        )

    @classmethod
    def del_list_choice_player_tournament(cls, players, tournament_players):
        print("Liste des joueurs\n")

        for player in players:
            if player not in tournament_players:
                print("Joueur  : " + player.name)

        print("\n")
        print("Liste des joueurs déjà inscrit au tournoi\n")

        for i, player in enumerate(tournament_players):
            print("Joueur n° " + str(i) + " : " + player.name)

        print("\n")

        return input("Supprimer un joueur du tournoi en entrant son numéro ou\n")

    @classmethod
    def detail_player(cls, player):
        print("Nom: " + player.name + "\n")
        print("Prénom: " + player.first_name + "\n")
        print("Date de naissance: " + player.date_of_birth + "\n")
        print("Sexe: " + player.type + "\n")
        print("Rang: " + str(player.ranking) + "\n")

    @classmethod
    def edit_player_view(cls, player):
        PlayersView.detail_player(player)
        return input(
            "Taper la première lettre du paramètre à modifier "
            "(Exemple pour Nom, taper n)\n"
        )

    @classmethod
    def edit_list_player_view(cls, players):

        for i, player in enumerate(players):
            print("Joueur n° " + str(i) + " : " + player.name)

        return input("Taper le numéro du joueur à modifier\n")

    @classmethod
    def list_player_score_view(cls, players_score):

        if players_score:
            print("Liste des joueurs\n")
        i = 0
        for player, score in players_score.items():
            print(
                "Joueur n° " + str(i) + " : " + str(player) + " , Score : " + str(score)
            )
            i = i + 1

        print("\n")
