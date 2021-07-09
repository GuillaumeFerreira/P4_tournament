class Tournament:


    def __init__(self, name, place, start, end, nb_tour, playeurs, description, time_type, tours):

        self.name = name
        self.place = place
        self.start = start
        self.end = end
        self.playeurs = playeurs
        self.description = description
        self.time_type = time_type
        self.tours = tours
        if nb_tour is None:
            self.nb_tour = 4
        else:
            self.nb_tour = nb_tour


