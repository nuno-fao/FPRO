def adigits(n1, n2, n3):
    int(n1), int(n2), int(n3)
    maximo = max(n1,n2,n3)
    minimo = min(n1,n2,n3)
    if (n3==maximo and n1==minimo) or (n1==maximo and n3==minimo):
        return int(maximo+str(n2)+minimo)
    if (n3==maximo and n2==minimo) or (n2==maximo and n3==minimo):
        return int(maximo+str(n1)+minimo)
    if (n2==maximo and n1==minimo) or (n1==maximo and n2==minimo):
        return int(maximo+str(n3)+minimo)
print(adigits("0","0","0"))
print ( int("004"))