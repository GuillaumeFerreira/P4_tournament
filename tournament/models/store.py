from models.players import Players
from models.tournament import Tournament


class Store:
    def __init__(self):
        self.data = {"players": [], "tournaments": []}

    def store_test(self):
        self.data["players"] = [
            Players("Dupond", "Jean", "04/07/1978", "M", 45),
            Players("Moulin", "Robert", "02/04/1986", "M", 89),
            Players("Bertin", "François", "08/11/1982", "M", 189),
            Players("Legrand", "Richard", "15/01/1990", "M", 35),
            Players("Lambert", "Delphine", "25/02/1988", "F", 115),
            Players("Garnier", "Marine", "12/03/1992", "F", 58),
            Players("Rousseau", "Laurie", "09/06/1983", "F", 72),
            Players("Dubois", "Isabelle", "04/09/1968", "F", 34),
        ]
        self.data["tournaments"] = [
            Tournament("Tournoi test", "Toulouse", "Tournoi fictif", "blitz")
        ]
