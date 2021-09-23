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

    def store_test(self):
        self.data["players"] = [
            Players("Dupond", "Jean", "04/07/1978", "M", 45, 0),
            Players("Moulin", "Robert", "02/04/1986", "M", 89, 0),
            Players("Bertin", "François", "08/11/1982", "M", 189, 0),
            Players("Legrand", "Richard", "15/01/1990", "M", 35, 0),
            Players("Lambert", "Delphine", "25/02/1988", "F", 115, 0),
            Players("Garnier", "Marine", "12/03/1992", "F", 58, 0),
            Players("Rousseau", "Laurie", "09/06/1983", "F", 72, 0),
            Players("Dubois", "Isabelle", "04/09/1968", "F", 34, 0),
        ]

        self.data["tournaments"] = [
            Tournament(
                "Tournoi test",
                "Toulouse",
                "Tournoi fictif",
                "blitz",
                self.data["players"],
                [
                    Round(
                        [
                            Match(
                                self.data["players"][0],
                                self.data["players"][1],
                            ),
                            Match(
                                self.data["players"][2],
                                self.data["players"][3],
                            ),
                            Match(
                                self.data["players"][4],
                                self.data["players"][5],
                            ),
                            Match(
                                self.data["players"][6],
                                self.data["players"][7],
                            ),
                        ]
                    )
                ],
            )
        ]

    def load_tournament(self, tournament):
        self.data["tournaments"].append(tournament)

    def search_player(self, id):
        for player in self.data["players"]:
            if player.id == id:
                return player

    def read_json(self):
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
