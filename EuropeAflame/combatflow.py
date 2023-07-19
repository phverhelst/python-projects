import random

def d10():
    x = random.randint(0,9)
    return x

class unit:
    
    def __init__(self, strength, damage):
        self.strength = strength
        self.damage = damage

unit1 = unit(5, 1)
unit2 = unit(5, 1)

x = (unit1.strength)
y = (unit2.strength)

#armygroup = [unit1, unit2]

#def round(unit1, unit2):

def attacking(strength):
    print("strength of the unit:",strength)
    roll = d10()
    print("result of the dice:",roll)
    if roll == 0:
        hit = (True, False)
    elif roll == 1 and strength >= 1 :
        hit = (True, True)
    elif roll ==9:
        hit = (False, False)
    elif roll <= strength:
        hit = (True, False)
    else:
        hit = (False, False)
    return hit

# attacker phase

print("Attacker phase")
print("--------------")

x = (attacking(unit1.strength))

print("Hit ?:", x[0])
print("Additionnal effect ?:", x[1])


# defender phase

print("Defender Counter-attacks")
print("------------------------")



y = (attacking(unit1.strength))

print("Hit ?:", y[0])
print("Additionnal effect ?:", y[1])

# losses assignments

print("Attacker losses assignments")
print("---------------------------")


print("Defender losses assignments")
print("---------------------------")



# 


# attack outcome








