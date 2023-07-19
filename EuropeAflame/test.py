import random

def d10():
    x = random.randint(0,9)
    return x

def attacking(strength):
    strenght = int(strength)
    roll = d10()
    print(roll)
    if roll == 0:
        hit = True
    elif roll <=9:
        hit = False
    elif roll == strength:
        hit = True
    else:
        hit = False
    return hit

print(attacking(5))