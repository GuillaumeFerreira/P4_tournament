class MatchView:
    @classmethod
    def match_list(cls, matchs):

        for i, match in enumerate(matchs):
            print(
                "Match n° "
                + str(i)
                + " - "
                + match.first_player.name
                + " vs "
                + match.second_player.name
            )

    @classmethod
    def winner_match(cls, matchs):

        for i, match in enumerate(matchs):
            print(
                "\nMatch n° "
                + str(i)
                + " - "
                + match.first_player.name
                + " (choix : 1)"
                + " vs "
                + match.second_player.name
                + " (choix : 2)"
            )
            winner = input(
                "Entrer votre choix du joueur gagnant ou 0 si égalité,"
                " sauvegarder le tournoi en entrant 's' \n"
            )
            if winner == "1":
                match.first_player.score = match.first_player.score + 1
                match.winner = match.first_player.id

            elif winner.lower() == "s":

                break

            elif winner == "0":
                # Egalité
                match.winner = None
            else:
                match.second_player.score = match.second_player.score + 1
                match.winner = match.second_player.id

        return winner
