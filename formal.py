def formal(name):
    lista = name.split(" ")
    length = len(lista)
    final = lista[length-1] + ","
    for n in range (length-1):
        final = final + " " + lista[n][0:1] + "."
    return final