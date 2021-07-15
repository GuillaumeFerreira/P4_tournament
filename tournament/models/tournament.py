import time

class Tournament:


    def __init__(self, name, place, players, description, time_type):

        self.name = name
        self.place = place
        self.start = time.now()
        self.end = None
        self.players = players
        self.description = description
        self.time_type = time_type
        self.tours = []

    def edit_end(self, days):
        self.end = self.start + days




