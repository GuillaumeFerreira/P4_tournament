from models.players import Players
from models.tournament import Tournament
from models.match import Match
from models.round import Round
import json
import os


class Store:
    def __init__(self):

        self.data = {"players": [], "tournaments": []}
        self.read_json()



    def search_player(self, id):
        for player in self.data["players"]:
            if player.id == id:
                return player

    def read_json(self):
        # tinydb
        tournaments_file = os.listdir("save/")
        data = {}

        f = open("save/players_data.json")
        data_load = json.load(f)

        for players in data_load["players"]:

            self.data["players"].append(
                Players(
                    players["name"],
                    players["first_name"],
                    players["date_of_birth"],
                    players["type"],
                    players["ranking"],
                    players["score"],
                    players["id"],
                )
            )

        for tournament_file in tournaments_file:
            if tournament_file != "players_data.json":
                f = open("save/" + tournament_file)
                data = json.load(f)
                players_tournament = []
                rounds_tournament = []

                for id in data["players"]:
                    players_tournament.append(self.search_player(id))

                for round in data["tournament"]["round"]:

                    list_matchs = []
                    for match in round["matchs"]:
                        list_matchs.append(
                            Match(
                                self.search_player(match["first_player"]),
                                self.search_player(match["second_player"]),
                                match["winner"],
                            )
                        )

                    rounds_tournament.append(Round(list_matchs))

                self.data["tournaments"].append(
                    Tournament(
                        data["tournament"]["name"],
                        data["tournament"]["place"],
                        data["tournament"]["description"],
                        data["tournament"]["time_type"],
                        players_tournament,
                        rounds_tournament,
                    )
                )
