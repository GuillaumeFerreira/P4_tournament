class Match:
    id = 0

    def __init__(self, first_player, second_player):
        self.id = Match.id
        Match.id = Match.id + 1
        self.first_player = first_player
        self.second_player = second_player
        self.winner = ""
