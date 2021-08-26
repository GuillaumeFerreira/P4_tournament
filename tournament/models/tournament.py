import time


class Tournament:
    def __init__(self, name, place, description, time_type, players=None, rounds=None):
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
                    match.first_player.name == first_player
                    and match.second_player.name == second_player
                ):
                    # print("match déjà joué, joueur 1 " + match.first_player.name + " = " + first_player + "joueur 2 " + match.second_player.name + " = "+ second_player )
                    return True
                elif (
                    match.first_player.name == second_player
                    and match.second_player.name == first_player
                ):
                    # print("match déjà joué, joueur 1 " + match.first_player.name + " = " + first_player + "joueur 2 " + match.second_player.name + " = "+ second_player )
                    return True

        return False

    def next_round(self, players):
        available_players = sorted(
            players, key=lambda player: (player.score, player.ranking), reverse=True
        )
        list_player_match = []

        while available_players:
            current_player = available_players.pop(0)  # 6

            for i, player in enumerate(available_players):
                if not self.has_played(current_player.name, player.name):
                    player_match = available_players.pop(i)
                    break
            list_player_match.append(current_player)
            list_player_match.append(player_match)

        return list_player_match

        