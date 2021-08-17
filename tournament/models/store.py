from models.players import Players
from models.tournament import Tournament
from models.match import Match
from models.round import Round
import json


class Store:
    def __init__(self):
        self.data = {"players": [], "tournaments": []}

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
            Tournament("Tournoi test", "Toulouse", "Tournoi fictif", "blitz",[
            Players("Dupond", "Jean", "04/07/1978", "M", 45, 1),
            Players("Moulin", "Robert", "02/04/1986", "M", 89, 0),
            Players("Bertin", "François", "08/11/1982", "M", 189, 1),
            Players("Legrand", "Richard", "15/01/1990", "M", 35, 1),
            Players("Lambert", "Delphine", "25/02/1988", "F", 115 , 0),
            Players("Garnier", "Marine", "12/03/1992", "F", 58, 0),
            Players("Rousseau", "Laurie", "09/06/1983", "F", 72, 1),
            Players("Dubois", "Isabelle", "04/09/1968", "F", 34, 0),
        ],[Round([Match(Players("Dupond", "Jean", "04/07/1978", "M", 45, 1), Players("Lambert", "Delphine", "25/02/1988", "F", 115, 0)),
                  Match(Players("Moulin", "Robert", "02/04/1986", "M", 89, 0), Players("Bertin", "François", "08/11/1982", "M", 189, 1)),
                  Match(Players("Legrand", "Richard", "15/01/1990", "M", 35, 1), Players("Garnier", "Marine", "12/03/1992", "F", 58, 0)),
                  Match(Players("Rousseau", "Laurie", "09/06/1983", "F", 72, 1), Players("Dubois", "Isabelle", "04/09/1968", "F", 34, 0))
                  ])])
        ]

    def load_tournament(self, tournament):
        self.data["tournaments"].append(tournament)

    def read_json(self):
        # Opening JSON file
        f = open("data.json")

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Iterating through the json
        # list
        player_tournament=[]
        round_tournament=[]
        for i in data["data"]:
            print(i)
            for player in i["Players"]:
                player_tournament.append(Players(player["name"],player["first_name"],player["date_of_birth"],player["type"],player["ranking"],player["score"]))

            self.load_tournament(Tournament(i["Tournament"]["name"],i["Tournament"]["place"],i["Tournament"]["description"],i["Tournament"]["time_type"],player_tournament, ))

        # Closing file
        f.close()
