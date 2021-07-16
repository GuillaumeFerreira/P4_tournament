import time

class Tournament:


    def __init__(self, name, place, description, time_type):

        self.name = name
        self.place = place
        self.start = time.localtime()
        self.end = None
        self.players = []
        self.description = description
        self.time_type = time_type
        self.tours = []

    def edit_end(self, days):
        self.end = self.start + days

    def get_params(self):
        print("\nParamètres du tournoi\n")
        print("Nom : " + self.name)
        print("Ville : " + self.place)
        print("Description : " + self.description + "\n")





