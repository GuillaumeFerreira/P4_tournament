class Players:

    id = 0

    def __init__(self, name, first_name, date_of_birth, type, ranking, score):

        self.id = Players.id
        Players.id = Players.id + 1
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.type = type
        self.ranking = ranking
        self.score = score
