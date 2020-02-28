def roman_to_integer(astring):
    conversion = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    out=0
    for i in range(len(astring)-1):
        if conversion[astring[i]]>=conversion[astring[i+1]]:
            out += conversion[astring[i]]
        else:
            out -= conversion[astring[i]]
    out += conversion[astring[-1]]
    return out