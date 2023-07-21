#armygroup = [unit1, unit2]

import random
from combat import *
from gameparts import *

def apply_dammages(grp_unit, damage_total):
    
    show_units(grp_unit)
    
    y = len(grp_unit)
    # print(y)
    
    is_unit_destroyed = False

    while True:
        try:
            x = int(input("Choose unit number: "))
        except ValueError:
            continue
        if x >= y or x < 0:
            continue
        else:
            break
    unit_strength = grp_unit[x].strength
    print("Strenght of the unit:", unit_strength)
    
    if damage_total > unit_strength:
        damages_possible = unit_strength
    else:
        damages_possible = damage_total
    print("Damages possible to assign:", damages_possible )
    
    while True:
        try:
            z = int(input("choose damages done to the unit: "))
        except ValueError:
            continue
        if z > damages_possible or z <= 0:
            continue
        # elif z <= 0:
        #     continue
        else:
            break

    unit_strength = unit_strength - z
    print("New total strenght of the unit:", unit_strength)
    grp_unit[x].strength = unit_strength
    last_known_unit_strenght = grp_unit[x].strength
    if grp_unit[x].strength == 0 :
        is_unit_destroyed = True
        del grp_unit[x]
  
    damage_total = damage_total - z

    # return [grp_unit[x].strength, is_unit_destroyed, damage_total]
    print([last_known_unit_strenght, is_unit_destroyed, damage_total])

def apply_retreat_units(grp_unit, retreat_result):
    
    show_units(grp_unit)
    y = len(grp_unit)

    while True:
        try:
            x = int(input("Choose unit number: "))
        except ValueError:
            continue
        if x >= y or x < 0:
            continue
        else:
            break
    
    grp_unit[x].is_retreating = True
    retreat_result -= 1


    # return [grp_unit[x], grp_unit[x].is_retreating, retreat_result]
    print ([grp_unit[x], grp_unit[x].is_retreating, retreat_result])

def remove_retreated_units(grp_unit):
    
    show_units(grp_unit)
    y = len(grp_unit)
    print(y)

    unit_to_pop = []

    for x in reversed(range(0, y)):
         if (grp_unit[x].is_retreating) == True:
             unit_to_pop.append(x)

    print(unit_to_pop)
    
    z = len(unit_to_pop)
    for x in range(0, z):
        grp_unit.pop(x)


def apply_retreat_points(grp_unit, retreat_result):
    pass
    

def ending_round():
    pass



# unit1 = Unit("infantry", 3, 1, "germany", True)
# unit2 = Unit("infantry", 4, 1, "germany", True)
unit3 = Unit("infantry", 6, 1, "germany", True)
unit4 = Unit("infantry", 3, 1, "germany", True)

unit1 = Unit("infantry", 3, 1, "germany", False)
unit2 = Unit("infantry", 4, 1, "germany", False)
# unit3 = Unit("infantry", 6, 1, "germany", False)
# unit4 = Unit("infantry", 3, 1, "germany", False)
unit5 = Unit("infantry", 4, 1, "germany", False)
unit6 = Unit("infantry", 6, 1, "germany", False)

unit11 = Unit("infantry", 5, 1, "poland", False)
unit12 = Unit("infantry", 2, 1, "poland", False)
unit13 = Unit("infantry", 4, 1, "poland", False)
unit14 = Unit("infantry", 5, 1, "poland", False)
unit15 = Unit("infantry", 2, 1, "poland", False)
unit16 = Unit("infantry", 4, 1, "poland", False)


# units_grp1 =[unit1, unit2, unit3, unit4, unit5, unit6]
units_grp1 =[unit1, unit2, unit3, unit4]
# units_grp1 =[unit1, unit2]
# units_grp1 =[unit1]

# units_grp2 =[unit11, unit12, unit13, unit14, unit15, unit6]
# units_grp2 =[unit11, unit12, unit13, unit14]
units_grp2 =[unit11, unit12]
# units_grp2 =[unit11]

attacker = fighting(units_grp1, True)
print("attacker",attacker)
defender = fighting(units_grp2, False)
print("defender", defender)

# show_units(units_grp1)

# apply_dammages(units_grp2, attacker[0])

# show_units(units_grp2)

# apply_retreat_units(units_grp1, defender[2])
# show_units(units_grp1)

remove_retreated_units(units_grp1)
show_units(units_grp1)
