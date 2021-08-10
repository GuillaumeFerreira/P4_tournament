from views.players_view import PlayersView


class RoundView:
    @classmethod
    def round_view(cls, players, nb_round):
        print("Round n°" + str(nb_round))
        PlayersView.list_player_score_view(players)

    @classmethod
    def winner(cls, players):
        sorted_list = sorted(players, key=lambda player: player.score, reverse=True)
        print(
            "Le gagnant du tournoi est "
            + sorted_list[0].name
            + " avec un score de "
            + str(sorted_list[0].score)
            + "\n"
        )
        print("Classement :\n")
        i = 1
        for player in sorted_list:
            print(
                str(i)
                + " .Nom : "
                + player.name
                + " ,Score : "
                + str(player.score)
                + "\n"
            )
            i = i + 1
