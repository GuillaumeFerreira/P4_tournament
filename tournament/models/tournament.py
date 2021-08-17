import time


class Tournament:
    def __init__(self, name, place, description, time_type, players, rounds):

        self.name = name
        self.place = place
        self.start = time.localtime()
        self.end = None
        self.players = players
        self.description = description
        self.time_type = time_type
        self.rounds = rounds

    def init_rounds(self, rounds):
        self.rounds = rounds

    def edit_end(self, days):
        self.end = self.start + days

    def has_played(self, first_player, second_player):
        played = False
        for round in self.rounds:
            for match in round.matchs:
                if (
                    match.first_player.name == first_player
                    and match.second_player.name == second_player
                ):
                    # print("match déjà joué, joueur 1 " + match.first_player.name + " = " + first_player + "joueur 2 " + match.second_player.name + " = "+ second_player )
                    played = True
                elif (
                    match.first_player.name == second_player
                    and match.second_player.name == first_player
                ):
                    # print("match déjà joué, joueur 1 " + match.first_player.name + " = " + first_player + "joueur 2 " + match.second_player.name + " = "+ second_player )
                    played = True
                else:
                    pass
                    # print("match non joué, joueur 1 " + match.first_player.name + " = " + first_player + "joueur 2 " + match.second_player.name + " = "+ second_player )
        return played

    def next_round(self, players):
        sorted_list = sorted(
            players, key=lambda player: (player.score, player.ranking), reverse=True
        )
        i = 0
        while self.has_played(sorted_list[i].name, sorted_list[i + 1].name) and i <= 8:

            exchange = sorted_list[i + 1]
            sorted_list[i + 1] = sorted_list[i - 1]
            sorted_list[i - 1] = exchange
            i = i + 2

        return sorted_list
