class Enemy:
    id_s = 0
    def __init__(self, name):
        self.name = name
        Enemy.id_s+=1
        self.id = Enemy.id_s
 
    def __str__(self):
        return f"{self.id}"