class Match:
    # id = 0

    def __init__(self, first_player, second_player, winner=None, id=None):
        if winner is None:
            self.winner = None
        else:
            self.winner = winner

        # self.id = Match.id
        # Match.id = Match.id + 1
        self.first_player = first_player
        self.second_player = second_player

    def to_dict(self):
        return {
            "first_player": self.first_player.id,
            "second_player": self.second_player.id,
            "winner": self.winner,
        }
