import random

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

def show_units(grp_unit):
    
    for x in range(0, len(grp_unit)):
        a = (grp_unit[x].strength)
        b = (grp_unit[x].is_retreating)
        print(x, a, b)

def input_a_value(len_of_grp_unit, list = []):
    while True:
        try:
            x = int(input("Choose unit number: "))
        except ValueError:
            continue
        if x >= len_of_grp_unit or x < 0:
            continue
        if test_if_in_list(list, x) == True:
            continue
        else:
            break
    return(x)

def test_if_in_list(list_name, value_to_check):

    is_present = False
    for x in list_name:
        # print(x)
        if x == value_to_check:
            is_present = True
    return is_present

def apply_retreat_points(grp_unit, points_must_retreating):
    
    show_units(grp_unit)
    len_grp = len(grp_unit)
    total_grp_strength = 0
    units_selected = []
    total_of_points_retreating = 0
    
    for y in range(0,len_grp):
        total_grp_strength = total_grp_strength + grp_unit[y].strength

    if len_grp == 1 :
        grp_unit[0].is_retreating = True
    
    elif points_must_retreating >= total_grp_strength:
            for z in range(0, len_grp):
                grp_unit[z].is_retreating = True
    else:
        while True:
            z = input_a_value(len_grp, units_selected)
            units_selected.append(z)
            print(units_selected)
            print(grp_unit[z].strength)
            total_of_points_retreating = total_of_points_retreating + grp_unit[z].strength
            print(total_of_points_retreating)
            if total_of_points_retreating >= points_must_retreating:
                break
    
    for w in units_selected:
        grp_unit[w].is_retreating = True

def apply_retreat_units(grp_unit, number_of_retreats):
    
    show_units(grp_unit)
    y = len(grp_unit)
    units_selected = []
    
    while True:
        z = input_a_value(y, units_selected)
        units_selected.append(z)
        number_of_retreats -= 1
        if number_of_retreats == 0:
            break

    for w in units_selected:
        grp_unit[w].is_retreating = True

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