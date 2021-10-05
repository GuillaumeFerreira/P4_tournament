import time


class Tournament:
    def __init__(
        self, name, place, description, time_type, players=None, rounds=None
    ):
        if players is None:
            players = []
        if rounds is None:
            rounds = []
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

        for round in self.rounds:
            for match in round.matchs:
                if (
                    match.first_player == first_player
                    and match.second_player == second_player
                ):
                    return True
                elif (
                    match.first_player == second_player
                    and match.second_player == first_player
                ):
                    return True

        return False

    def next_round(self):

        available_players = sorted(
            self.players,
            key=lambda player: (player.score, player.ranking),
            reverse=True,
        )
        list_player_match = []

        while available_players:
            current_player = available_players.pop(0)

            for i, player in enumerate(available_players):
                if not self.has_played(current_player.name, player.name):
                    # match
                    player_match = available_players.pop(i)
                    break
            list_player_match.append(current_player)
            list_player_match.append(player_match)

        return list_player_match

    def to_dict(self):
        return {
            "name": self.name,
            "place": self.place,
            "start": self.start,
            "end": self.end,
            "players": [player.to_dict() for player in self.players],
            "description": self.description,
            "time_type": self.time_type,
            "round": [round.to_dict() for round in self.rounds],
        }
