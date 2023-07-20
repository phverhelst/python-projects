#armygroup = [unit1, unit2]

import random

class Unit:
    
    def __init__(self, unit_type, strength, damage, nationality):
        self.unit_type = unit_type
        self.strength = strength
        self.damage = damage
        self.nationality = nationality

class Terrain:
    pass

def d10():
    x = random.randint(0,9)
    print("Dice result:",x)
    return x

def combat(strength):
    print("Unit strength:",strength)
    roll = d10()
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
    # print("Hit ?", hit[0], "\nIs a 1?", hit[1])
    return hit

def damage(is_attacker, result, add_effect, unit_damages):
    if result == True and is_attacker == True:
        x = (1 * unit_damages)
    elif result == True and is_attacker == False and add_effect == False:
        x = (1 * unit_damages)
    elif result == True and is_attacker == False and add_effect == True:
        x = (1 * unit_damages) + 1
    else:
        x = 0
    # print("Is attacker?", is_attacker)
    # print("Damage done by the unit:", unit_damages)
    # print("Number of damages done:", x)
    return x

def retreat(is_attacker,result, add_effect, unit_strength):
    if result == True and is_attacker == True and add_effect == True:
        x = unit_strength
    elif result == True and is_attacker == False and add_effect == False:
        x = False
    elif result == True and is_attacker == False and add_effect == True:
        x = True
    else:
        x = 0
    # print("The retreat result is:", x)
    # if x == True or x == False:
    #     print("The attacker must retreat a unit ?", x)
    # else:
    #     print("How much strength points the defender must retreat ?", x)
    return x

def round_attack (unit, is_attacking):
    
    x = combat(unit.strength)
    y = damage(is_attacking, x[0], x[1], unit.damage)
    z = retreat(is_attacking, x[0], x[1], unit.strength)
    return [y, z]

def fighting (grp_units, is_attacking):
    
    total_damages = 0
    total_retreating_points = 0
    total_retreats = 0
    
    for x in range(0, len(grp_units)):
        a = (round_attack(grp_units[x], is_attacking))
        # print(a)
        # print(a[0])
        # print(a[1])
        total_damages = total_damages + a[0]
        if is_attacking == True:
            total_retreating_points = total_retreating_points + a[1]
        else:
            if a[1] == True:
                total_retreats += 1
    
    # print("*************************")
    # print(total_damages)
    # print(total_retreating_points)
    # print(total_retreats)

    return [total_damages, total_retreating_points, total_retreats]


unit1 = Unit("infantry", 3, 1, "germany")
unit2 = Unit("infantry", 4, 1, "germany")
unit3 = Unit("infantry", 6, 1, "germany")
unit4 = Unit("infantry", 5, 1, "poland")
unit5 = Unit("infantry", 2, 1, "poland")
unit6 = Unit("infantry", 4, 1, "poland")

# units_grp1 =[unit1, unit2, unit3, unit1, unit2, unit3]
# units_grp2 =[unit4, unit5, unit6, unit4, unit5, unit6]

units_grp1 =[unit1]
units_grp2 =[unit4]

print(fighting(units_grp1, True))
print(fighting(units_grp2, False))

