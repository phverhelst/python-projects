import random
from combat import *
from gameparts import *

unit3 = Unit("infantry", 6, 1, "germany", False)
unit4 = Unit("infantry", 3, 1, "germany", False)
unit1 = Unit("infantry", 3, 1, "germany", False)
unit2 = Unit("infantry", 4, 1, "germany", False)

# units_grp1 =[unit1]
units_grp1 =[unit1, unit2, unit3, unit4]
list = []

def test_if_in_list(list_name, value_to_check):

    is_present = False
    for x in list_name:
        # print(x)
        if x == value_to_check:
            is_present = True
    return is_present

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
            if total_of_points_retreating > points_must_retreating:
                break
            

    show_units(grp_unit)
    print(units_selected)
    
    
    
    # while total_of_points_to_retreat <
    # input_a_value(x)

# list=[0,1,2]
# input_a_value(5, list)

# print(test_if_in_list(list, 3))
apply_retreat_points(units_grp1, 7)


# y = len(grp_unit)

# while total_selected <= total_to_get:
#         print("first loop")
#         while True:
#             try:
#                 x = int(input("Choose unit number: "))
#             except ValueError:
#                 print("ValueError")
#                 continue
#             if x >= y or x < 0:
#                 print("x >= y or x < 0", x, y )
#             else:





# apply_retreat_points(units_grp1, 10)


#     y = len(grp_unit)
#     print("y value:", y)
#     total_to_get = retreat_result
#     print("total_to_get:", total_to_get)
#     units_selected = []
#     units_selected_length = len(units_selected)
#     print(units_selected_length)

#     total_selected = 0
#     print("total_selected:", total_selected)

#     while total_selected <= total_to_get:
#         print("first loop")
#         while True:
#             try:
#                 x = int(input("Choose unit number: "))
#             except ValueError:
#                 print("ValueError")
#                 continue
#             if x >= y or x < 0:
#                 print("x >= y or x < 0", x, y )
#             else:
#                 print("x:", x)
#                 print("units_selected_length:", units_selected_length)
#                 if units_selected_length > 0:
#                     for w in units_selected:
#                         print(w)
#                         if x == units_selected[w]:
#                             continue
#                 units_selected.append(x)
#                 units_selected_length = len(units_selected)
#                 print(units_selected)
#                 print("break")
#                 break 
            

    #         total_selected = total_selected + grp_unit[x].strength
    #         print(total_selected)
    #         continue
    # print(units_selected)