class Player:
    id_s = 0
    def __init__(self, name):
        self.name = name
        Player.id_s+=1
        self.id = Player.id_s
 
    def __str__(self):
        return f"{self.id}"