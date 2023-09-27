class Wall:
    id_s = 0

    def __init__(self, type):
        self.type = type
        Wall.id_s += 1
        self.id = Wall.id_s

    def __str__(self):
        return f"{self.id}"