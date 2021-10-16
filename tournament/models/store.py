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
                players_tournament.append(self.search_player(player))

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

    # Sauvegarde d'un tournoi dans la bdd
    def save_json(self, tournament):
        # utilisation de tinydb
        if self.db.table("Tournament").search(Query().name == tournament.name):
            # Modification du tournoi
            self.del_tournament(tournament)
            self.add_tournament(tournament)
        else:
            # Ajout du tounoi
            self.add_tournament(tournament)

    #########################################################
    #           AJOUT,MODIFICATION ET SUPPRESSION           #
    #               DANS BASE DE DONNEES                    #
    #########################################################
    def update_player_param(self, player, key, value):

        player_table = self.db.table("players")
        query = Query()
        player_table.update({key: int(value)}, query.id == player.id)

    def add_player_bdd(self, player):

        player_table = self.db.table("players")
        player_table.insert(player.to_dict())

    def del_player_bdd(self, player):

        player_table = self.db.table("players")
        query = Query()
        player_table.remove(query.id == player.id)

    def update_tournament_param(self, tournament, key, value):
        self.db.table("Tournament").update(
            {key: value}, Query().name == tournament.name
        )

    def add_tournament(self, tournament):

        tournament_table = self.db.table("Tournament")
        tournament_table.insert(tournament.to_dict())

    def del_tournament(self, tournament):

        tournament_table = self.db.table("Tournament")
        query = Query()
        tournament_table.remove(query.name == tournament.name)

    #########################################################
    #           VUE DE LA BASE DE DONNEES                   #
    #########################################################
    def vue_tournament(self):

        tournament_table = self.db.table("Tournament")
        return tournament_table.all()

    def vue_players_tournament(self, tournament):

        players = []
        for player in self.db.table("Tournament").search(
            Query().name == tournament["name"]
        )[0]["players"]:
            players.append(self.search_player(player))

        return players

    def vue_tournament_match(self, tournament):

        dict_match_tournament = {}
        for round in self.db.table("Tournament").search(
            Query().name == tournament["name"]
        )[0]["round"]:
            round_name = round["name"]
            tab_name = []
            for match in round["matchs"]:
                tab_name.append(
                    [
                        self.search_player(match["first_player"]).name,
                        self.search_player(match["second_player"]).name,
                    ]
                )

            dict_match_tournament[round_name] = tab_name

        return dict_match_tournament

    def vue_tournament_round(self, tournament):

        round_names = []
        for round in self.db.table("Tournament").search(
            Query().name == tournament["name"]
        )[0]["round"]:
            round_names.append(round["name"])

        return round_names

    def vue_players(self):

        players = []
        for player in self.db.table("players").all():

            players.append(
                Players(
                    player["name"],
                    player["first_name"],
                    player["date_of_birth"],
                    player["type"],
                    player["ranking"],
                    player["score"],
                    player["id"],
                )
            )

        return players
