class Unit:
    
    def __init__(self, unit_type, strength, damage, nationality, is_retreating):
        self.unit_type = unit_type
        self.strength = strength
        self.damage = damage
        self.nationality = nationality
        self.is_retreating = is_retreating

class Terrain:
    pass


# class unit:
    
#     def __init__(self, strength, move, damage):
#         self.strength = strength
#         self.move = move
#         self.damage = damage

# class shock(unit):

#     def __init__(self, strength, move, damage):
#         super().__init__(strength, move, damage)
#         self.type = "schock unit"

# x = shock(4,4,4)

# print(x.move)
# print(x.strength)
# print(x.damage)
