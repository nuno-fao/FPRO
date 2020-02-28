def unique(atuple):
    atuple = sorted(atuple)
    new_tuple = (atuple[0],)
    i = 0
    for n in atuple[1:]:
        if n!=atuple[i]:
            new_tuple += (n,)
        i += 1
    return new_tuple