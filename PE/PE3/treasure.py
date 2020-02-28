def treasure(clues):
    x=(0,0)
    while x in clues:
        temp=x
        x=clues[x]
        del clues[temp]
    return x
print(treasure({(0,0): (5,6), (7,8): (6,7), (5,6): (6,7), (6,7):
(7,8)}))