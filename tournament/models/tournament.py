import time
from views.round_view import RoundView
from views.match_view import MatchView
from models.round import Round
from models.match import Match


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
            current_player = available_players.pop(0)  # 6

            for i, player in enumerate(available_players):
                if not self.has_played(current_player.name, player.name):
                    # match
                    player_match = available_players.pop(i)
                    break
            list_player_match.append(current_player)
            list_player_match.append(player_match)

        RoundView.round_view(self.players, len(self.rounds) + 1)
        round = Round([])
        for i in range(0, 8, 2):
            round.matchs.append(
                Match(list_player_match[i], list_player_match[i + 1])
            )

        for round_view in self.rounds:
            MatchView.match_list(round_view.matchs)

        MatchView.match_list(round.matchs)

        # for match in round.matchs:
        # tournament.has_played(match.first_player.name,match.second_player.name)

        save = MatchView.winner_match(round.matchs)

        self.rounds.append(round)
        return save

    def to_dict(self):
        return {
            "name": self.name,
            "place": self.place,
            "start": self.start,
            "end": self.end,
            "description": self.description,
            "time_type": self.time_type,
            "round": [round.to_dict() for round in self.rounds],
        }
