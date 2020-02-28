def mastermind(g1, g2, g3, c1, c2, c3):
    soma = 0
    if g1==c1:
        soma +=3
    elif g1==c2 or g1==c3:
        soma +=1
    if g2==c2:
        soma +=3
    elif g2==c1 or g2==c3:
        soma +=1
    if g3==c3:
        soma +=3
    elif g3==c1 or g3==c2:
        soma +=1
    return soma
print(mastermind('b', 'w', 'y', 'b', 'b', 'b'))