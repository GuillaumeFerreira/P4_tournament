class MatchView:
    @classmethod
    def match_list(cls, matchs):
        i=1
        for match in matchs:
            print("Match n°" + str(i) + " - " + match.first_player.name + " vs " + match.second_player.name)
            i = i + 1

    @classmethod
    def winner_match(cls, matchs):
        i = 1
        for match in matchs:
            print("Match n°" + str(i) + " - " + match.first_player.name + " vs " + match.second_player.name)
            winner = input("Entrer le nom du Gagnant")
            if winner == match.first_player.name:
                match.first_player.score = match.first_player.score + 1
            i = i + 1
        return matchs