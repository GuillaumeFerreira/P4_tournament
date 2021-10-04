from models.players import Players
from models.tournament import Tournament
from models.match import Match
from models.round import Round
import json
import os
from tinydb import TinyDB,Query

class Store:
    def __init__(self):

        self.data = {"players": [], "tournaments": []}




    def search_player(self, id):

        for player in self.data["players"]:

            if player.id == id:
                return player
        #return next(player for player in self.data["players"] if player.id == id)

    def read_json(self):
        # tinydb
        #tournaments_file = os.listdir("save/")
        #data = {}


        db_players = TinyDB('save/bdd_tournament.json')
        player_table = db_players.table('players')
        results = player_table.all()
        for players in results:

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
        tournament_table = db_players.table('Tournament')

        results = tournament_table.all()
        for tournament in results:
            
            self.data["tournaments"].append(
                Tournament(
                    tournament["name"],
                    tournament["place"],
                    tournament["description"],
                    tournament["time_type"],
                    tournament["players"],
                    tournament['round'],
                ))
            """
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
                )"""

    def save_json(self, tournament):
        # utilisation de tinydb

        db_players = TinyDB('save/bdd_tournament.json')
        player_table = db_players.table('players')
        query = Query()
        for player in tournament.players:

            if player_table.search(query.id == player.id):
                #Le joueur existe déja, on ne le rajoute pas dans la base de donnée
                pass
            else:
                #On ajoute le joueur à la bdd
                player_table.insert(player.to_dict())


        tournament_table = db_players.table('Tournament')
        tournament_table.insert(tournament.to_dict())
        """
        f = open("save/players_data.json")
        data_load = json.load(f)
        data = {}
        list_id_player = []
        data["players"] = []

        for players in data_load["players"]:
            list_id_player.append(
                {
                    "id": players["id"],
                    "name": players["name"],
                    "first_name": players["first_name"],
                    "date_of_birth": players["date_of_birth"],
                    "type": players["type"],
                    "ranking": players["ranking"],
                    "score": players["score"],
                }
            )
            data["players"].append(players["id"])

        data_players = {}
        data["tournament"] = tournament.to_dict()

        data_players["players"] = list_id_player

        for i, player in enumerate(tournament.players):
            if player.id not in list_id_player[i]["id"]:
                data_players["players"].append(player.to_dict())

        with open("save/" + tournament.name + "_data.json", "w") as outfile:
            json.dump(data, outfile)

        with open("save/players_data.json", "w") as outfile:
            json.dump(data_players, outfile)"""