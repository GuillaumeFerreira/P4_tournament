class MatchView:
    @classmethod
    def match_list(cls, matchs):

        for match in matchs:
            print(
                "Match n° "
                + str(match.id)
                + " - "
                + match.first_player.name
                + " vs "
                + match.second_player.name
            )

    @classmethod
    def winner_match(cls, matchs):

        for match in matchs:
            print(
                "\nMatch n° "
                + str(match.id)
                + " - "
                + match.first_player.name
                + " (id : "
                + str(match.first_player.id)
                + ")"
                + " vs "
                + match.second_player.name
                + " (id : "
                + str(match.second_player.id)
                + ")"
            )
            winner = input("Entrer id du joueur gagnant ou sauvegarder le tournoi en entrant 's' \n")
            if winner == str(match.first_player.id):
                match.first_player.score = match.first_player.score + 1
            elif winner.lower() == 's':

                break
            else:
                match.second_player.score = match.second_player.score + 1


        return winner