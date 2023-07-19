import random

def d10():
    x = random.randint(0,9)
    return x

def combatround(strength):
    x = d10
    if x == 0:
        return [-1, False]
    elif x == 1:
        return [-1, True]
    else:
        return [0, False]

class unit:
    
    def __init__(self, strength, move, damage):
        self.strength = strength
        self.move = move
        self.damage = damage
        x = [self.strength, self.move, self.damage]
        return x

print(combatround(10))

x = unit(4,1,1)
print(x[0])





