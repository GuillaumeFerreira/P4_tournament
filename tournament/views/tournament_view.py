class TournamentView:
    @classmethod
    def tournament_view(cls, tournament):
        print("\nParamètres du tournoi\n")
        print("Nom : " + tournament.name)
        print("Ville : " + tournament.place)
        print("Description : " + tournament.description + "\n")
        print("Joueurs inscrits : " + str(len(tournament.players)) + "/8\n")

        print("1. Modifier les parametres du tournoi\n")
        print("2. Ajouter des joueurs au tournoi\n")
        print("3. Supprimer des joueurs au tournoi\n")
        print("4. Lancer le tournoi\n")
        print("5. Sauvegarder le tournoi\n")
        print("H. Revenir sur le menu principal\n")
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
        print("1 - Nom : " + tournament.name + "\n")
        print("2 - Ville : " + tournament.place + "\n")
        print("3 - Description : " + tournament.description + "\n")

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

        for i, tournament in enumerate(tournaments):
            if len(tournament.rounds) == 0:
                print(
                    str(i + 1)
                    + " - Nom : "
                    + tournament.name
                    + " | Nombre de Round déjà effectué "
                    + str(len(tournament.rounds))
                    + "\n"
                )
            else:
                print(
                    str(i + 1)
                    + " - Nom : "
                    + tournament.name
                    + " | Nombre de Round déjà effectué "
                    + str(len(tournament.rounds))
                    + "\n"
                )

        print("C. Créer un tournoi\n")
        print("S. Supprimer un tournoi\n")
        print("H. Revenir sur le menu principal\n")
        print("Q. Quitter le programme\n")

        return input(
            "Faire un choix en entrant une lettre "
            "ou modifier le un tournoi en entrant son numéro\n"
        )

    @classmethod
    def list_tournament_del(cls, tournaments):
        print("\nListe des tournois \n")

        for i, tournament in enumerate(tournaments):
            print(str(i + 1) + " - Nom : " + tournament.name + "\n")
        print("H. Revenir sur le menu principal\n")
        print("Q. Quitter le programme\n")

        return input("Choisir un tournoi à supprimer ")

    @classmethod
    def menu_rapport(cls):

        print("\n1 - Liste des joueurs en général par ordre alphabétique")
        print("2 - Liste des joueurs en général par classement")
        print("3 - Liste de tous les joueurs d'un tournoi par ordre alphabétique")
        print("4 - Liste de tous les joueurs d'un tournoi par classement")
        print("5 - Liste de tous les tounois")
        print("6 - Liste de tous les tours d'un tournoi")
        print("7 - Liste de tous les matchs d'un tournoi")
        print("H - Revenir sur le menu principal")
        print("Q - Quitter le programme\n")
        return input("Faire un choix\n")

    @classmethod
    def rapport_acteur_alpha(cls, players):
        print("\nListe des joueurs par ordre alphabétique")
        sorted_list = sorted(players, key=lambda player: player.name)
        for acteur in sorted_list:
            print(acteur.name)

    @classmethod
    def rapport_acteur_classement(cls, players):
        print("\nListe des joueurs par classement")
        sorted_list = sorted(players, key=lambda player: player.ranking)
        for acteur in sorted_list:
            print("Nom : " + acteur.name + " | Rang : " + str(acteur.ranking))

    @classmethod
    def rapport_players_tournament_alpha(cls, players):

        print("\nListe des joueurs du tounoi par ordre alphabétique")
        sorted_list = sorted(players, key=lambda player: player.name)
        for acteur in sorted_list:
            print(acteur.name)

    @classmethod
    def rapport_players_tournament_classement(cls, players):

        print("\nListe des joueurs du tounoi par classement")
        sorted_list = sorted(players, key=lambda player: player.ranking)
        for acteur in sorted_list:
            print("Nom : " + acteur.name + " | Rang : " + str(acteur.ranking))

    @classmethod
    def rapport_tournament(cls, tournaments):
        print("\nListe des tounois ")
        for tournoi in tournaments:
            print("\nNom : " + tournoi["name"])
            print("Ville : " + tournoi["place"])
            print("Type : " + tournoi["time_type"])
            print("Description : " + tournoi["description"])

    @classmethod
    def rapport_tournament_round(cls, round_names):
        print("\nListe des tours du tournoi\n")
        for round_name in round_names:
            print(round_name)

    @classmethod
    def rapport_tournament_match(cls, tournoi):
        print("\nListe des matchs du tournoi")
        for round, table_names in tournoi.items():
            print("\n" + round)
            for match in table_names:
                print(match[0] + " vs " + match[1])

    @classmethod
    def rapport_tournament_choice(cls, tournaments):
        for i, tournoi in enumerate(tournaments):
            print(str(i + 1) + " - Nom du tournoi " + tournoi["name"])

        n = input("\nChoississez votre tournoi\n")
        return tournaments[int(n) - 1]
