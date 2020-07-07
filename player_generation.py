it#B er her min shorthand for board, t er for det tvungne local board og won er bare for at i kan se at man kan hente den ind, jeg bruger den ikke her

def Player1(B, t, won): # En Bot som vælger det første mulig træk på boardet
    if t == 9:
        for i in range(9):
            if won[i] == 0 and any((True for x in B[i] if x == 0)) == True:
                a = i
                break
    else:
        a = t
    b = B[a].index(0)
    return a,b      ## a er midt index for hvilket local board vigtigt at vælge det tvungende local board mens b er den frit valgte. 
                    #£ Det er meget vigtigt at det bliver returneret på denne måde da definitionen af a og b i linje 56 og 58 i The_Arena ellers giver problemer

import numpy.random as rng

def Player2(B,t, won): # En Bot som vælger et tilfældigt træk blandt de mulige.
    if t == 9:
        list = []
        for i in range(9):
            if won[i] == 0 and any((True for x in B[i] if x == 0)) == True:
                list.append(i)
        a = rng.choice(list)
    else:
        a = t
    list =[]
    for i in range(9):
        if B[a][i] == 0:
            list.append(i)
    b = rng.choice(list)
    return a,b
