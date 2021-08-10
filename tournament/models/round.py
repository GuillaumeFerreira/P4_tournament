from operator import attrgetter
from models.match import Match


class Round:
    id = 0

    def __init__(self):
        self.id = Round.id
        Round.id = Round.id + 1
        self.matchs = []

    def init_round(self, players):

        # sorted_list = sorted(players, key=attrgetter("score", "ranking"))
        sorted_list = sorted(players, key=lambda player: player.ranking)
        first_list_players = sorted_list[0:4]
        second_list_players = sorted_list[4:8]
        for i in range(0, 4):
            self.matchs.append(Match(first_list_players[i], second_list_players[i]))

    def next_round(self, players):
        sorted_list = sorted(players, key=lambda player: player.score)

        for i in range(0, 8, 2):
            self.matchs.append(Match(sorted_list[i], sorted_list[i + 1]))
