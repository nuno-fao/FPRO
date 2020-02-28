def uppercase(astring):
    count = 0
    for n in astring[0:3]:
        if n==n.upper() and n!=n.lower():
            count += 1
    if count >= 1:
        astring = astring.upper()
    return astring