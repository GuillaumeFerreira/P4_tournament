class Players:

    id = 0

    def __init__(self, name, first_name, date_of_birth, type, ranking, score, id=None):
        if id is None:
            self.id = Players.id
            Players.id = Players.id + 1
        else:
            self.id = id

        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.type = type
        self.ranking = ranking
        self.score = score

    def to_dict(self):
        return {
            "name": self.name,
            "first_name ": self.first_name,
            "date_of_birth": self.date_of_birth,
            "type": self.type,
            "ranking": self.ranking,
            "score ": self.score,
        }
