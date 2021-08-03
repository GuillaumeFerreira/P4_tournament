class Match:
    def __init__(self, players):

        sorted_list = sorted(players, key=ranking)
        self.first_list_players = sorted_list[0:3]
        self.second_list_players = sorted_list[4:8]
