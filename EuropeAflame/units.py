class unit:
    
    def __init__(self, strength, move, damage):
        self.strength = strength
        self.move = move
        self.damage = damage

class shock(unit):

    def __init__(self, strength, move, damage):
        super().__init__(strength, move, damage)
        self.type = "schock unit"

x = shock(4,4,4)

print(x.move)
print(x.strength)
print(x.damage)
