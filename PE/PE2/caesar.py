def caesar(message):
    import math as m
    t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = ""
    for i,letter in enumerate(message):
        if letter==letter.lower():
            out+=letter
        elif letter!=letter.lower():
            n = ((1+m.sqrt(5))**i-(1-m.sqrt(5))**i)//(m.sqrt(5)*2**i)
            ind = t.index(letter)
            n= int((ind-n)%26)
            out += t[n]
    return out
print(caesar("CAESAR CIPHER"))