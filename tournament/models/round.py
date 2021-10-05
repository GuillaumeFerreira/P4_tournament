from models.match import Match


class Round:
    id = 0

    def __init__(self, matchs):

        Round.id = Round.id + 1
        self.matchs = matchs
        self.name = "Round " + str(Round.id)

    def init_round(self, players):

        sorted_list = sorted(players, key=lambda player: player.ranking)
        first_list_players = sorted_list[0:4]
        second_list_players = sorted_list[4:8]
        for i in range(0, 4):
            self.matchs.append(Match(first_list_players[i], second_list_players[i]))

    def to_dict(self):

        return {
            "name": self.name,
            "matchs": [match.to_dict() for match in self.matchs],
        }
