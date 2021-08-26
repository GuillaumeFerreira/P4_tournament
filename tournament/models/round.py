from models.match import Match


class Round:
    id = 0

    def __init__(self, matchs):

        self.id = Round.id
        Round.id = Round.id + 1
        self.matchs = matchs
        self.name = "Round " + str(self.id)

    def init_round(self, players):

        sorted_list = sorted(players, key=lambda player: player.ranking)
        first_list_players = sorted_list[0:4]
        second_list_players = sorted_list[4:8]
        for i in range(0, 4):
            self.matchs.append(Match(first_list_players[i], second_list_players[i]))

    def to_dict(self):
        return {"id": self.id, "name": self.name}


"""
    def next_round(self, players):
        #sorted_list = sorted(players, key=lambda player: (player.score, player.ranking), reverse=True)
        pass
        #for i in range(0, 8, 2):
            #verification si la paire est déja existante
            for match in matchs:
                if match.first_player == sorted_list[i].name and match.second_player == sorted_list[i+1].name:
                    print("match déjà joué")
                elif match.first_player == sorted_list[i+1].name and match.second_player == sorted_list[i].name:

        #self.matchs.append(Match(sorted_list[i], sorted_list[i + 1]))"""
