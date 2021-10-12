from models.players import Players
from models.tournament import Tournament
from models.match import Match
from models.round import Round
from tinydb import TinyDB, Query


class Store:
    def __init__(self):

        self.data = {"players": [], "tournaments": []}
        self.db = TinyDB("save/bdd_tournament.json")
    def search_player(self, id):

        for player in self.data["players"]:

            if player.id == id:
                return player


    def read_json(self):

        self.data = {"players": [], "tournaments": []}

        db_players = TinyDB("save/bdd_tournament.json")
        player_table = db_players.table("players")
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
        tournament_table = db_players.table("Tournament")

        results = tournament_table.all()

        for tournament in results:

            rounds_tournament = []
            for round in tournament["round"]:

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

            players_tournament = []

            for player in tournament["players"]:
                players_tournament.append(self.search_player(player["id"]))

            self.data["tournaments"].append(
                Tournament(
                    tournament["name"],
                    tournament["place"],
                    tournament["description"],
                    tournament["time_type"],
                    players_tournament,
                    rounds_tournament,
                )
            )

    def save_json(self, tournament):
        # utilisation de tinydb

        db_players = TinyDB("save/bdd_tournament.json")

        tournament_table = db_players.table("Tournament")
        query = Query()
        if tournament_table.search(query.name == tournament.name):
            # Modification du tournoi
            self.del_tournament(tournament)
            self.add_tournament(tournament)
        else:
            # Ajout du tounoi
            self.add_tournament(tournament)


    def update_player_param(self, player, key, value):
        db_players = TinyDB("save/bdd_tournament.json")
        player_table = db_players.table("players")
        query = Query()
        player_table.update({key: int(value)}, query.id == player.id)

    def add_player_bdd(self, player):
        db_players = TinyDB("save/bdd_tournament.json")
        player_table = db_players.table("players")
        player_table.insert(player.to_dict())

    def del_player_bdd(self, player):
        db_players = TinyDB("save/bdd_tournament.json")
        player_table = db_players.table("players")
        query = Query()
        player_table.remove(query.id == player.id)

    def update_tournament_param(self, tournament, key, value):
        self.db.table("Tournament").update({key: value}, Query().name == tournament.name)

    def add_tournament(self, tournament):
        db_players = TinyDB("save/bdd_tournament.json")
        tournament_table = db_players.table("Tournament")
        tournament_table.insert(tournament.to_dict())

    def del_tournament(self, tournament):
        db_players = TinyDB("save/bdd_tournament.json")
        tournament_table = db_players.table("Tournament")
        query = Query()
        tournament_table.remove(query.name == tournament.name)
