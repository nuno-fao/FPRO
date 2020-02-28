def genealogy(l):
    family = ["sibling","parent","cousin","grandparent"]
    l = sorted(l, key=lambda x: x[0])
    out = []
    for elem in family:
        for member in l:
            if member[1]==elem:
                out.append(member)
    return out
print(genealogy([("sofia", "sibling"), ("sara", "parent"), ("bernardo", "parent")]))