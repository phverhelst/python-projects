#armygroup = [unit1, unit2]

import random
from combat import *
from gameparts import *

def apply_dammage_sequence(grp_unit, damage_total):
    
    show_units(grp_unit)
    len_grp = len(grp_unit)
    total_force_grp = 0
    
    combatting_units = []
    for c in range(0, len_grp):
        combatting_units.append(grp_unit[c].strenght)
    print("combatting_units", combatting_units)
    
    units_destroyed = []

    for y in range(0, len_grp):
        total_force_grp = total_force_grp + grp_unit[y].strength

    if damage_total >= total_force_grp:
        for y in range(0, len_grp):
            units_destroyed.append(y)

    elif len_grp == 1:
        grp_unit[0].strength = grp_unit[0].strength - damage_total
        if grp_unit[0].strenght == 0:
            units_destroyed.append(0)

    else:
        print("end")

        # while True:
            
        #     z = input_a_value(len_grp, units_selected)
            
        #     unit_strength = grp_unit[z].strength
        #     print("Strenght of the unit:", unit_strength)
            
        #     a = damages_possible(grp_unit[z].strength, damage_total)
        #     print("Damages possible to assign:", a )
            
        #     b = simple_number_input(1, a)
        #     print("Damages assigned:", b )

        #     unit_strength = unit_strength - b
        #     print("New total strenght of the unit:", unit_strength)
            
        #     if unit_strength == 0:
        #         grp_unit[x].strength = unit_strength
        #         units_destroyed.append(x)
        #     last_known_unit_strenght = grp_unit[x].strength

        #     if grp_unit[x].strength == 0 :
        #         is_unit_destroyed = True
        # del grp_unit[x]
    
    print("units_destroyed", units_destroyed)
  
    # damage_total = damage_total - z

    # return [grp_unit[x].strength, is_unit_destroyed, damage_total]
    print([last_known_unit_strenght, is_unit_destroyed, damage_total])

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


# units_grp1 =[unit1, unit2, unit3, unit4, unit5, unit6]1
units_grp1 =[unit1, unit2, unit3, unit4]
# units_grp1 =[unit1, unit2]
# units_grp1 =[unit1]


# units_grp2 =[unit11, unit12, unit13, unit14, unit15, unit6]
# units_grp2 =[unit11, unit12, unit13, unit14]
units_grp2 =[unit11, unit12]
# units_grp2 =[unit11]

# attacker = fighting(units_grp1, True)
# print("attacker",attacker)
# defender = fighting(units_grp2, False)
# print("defender", defender)

show_units(units_grp2)
# apply_dammage_sequence(units_grp2, 20)

# show_units(units_grp2)

# apply_retreat_units(units_grp1, 2)
# show_units(units_grp1)

# remove_retreated_units(units_grp1)
# show_units(units_grp1)
# apply_retreat_points(units_grp1, 10)
