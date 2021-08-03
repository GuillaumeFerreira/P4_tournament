from operator import attrgetter
from models.match import Match
class Round:
    def __init__(self):
        self.matchs = []

    def init_round(self, players):

        sorted_list = sorted(players, key=attrgetter('ranking','score'))
        #sorted_list = sorted(players, key=lambda player: player.ranking)
        first_list_players = sorted_list[0:4]
        second_list_players = sorted_list[4:8]
        for i in range(0,4):
            self.matchs.append(Match(first_list_players[i], second_list_players[i]))




