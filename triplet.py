def triplet(atuple):
    for n in range(len(atuple)-2):
        for x in range(n+1,len(atuple)):
            for y in range(x+1,len(atuple)):
                if atuple[n]+atuple[x]+atuple[y]==0:
                    return (atuple[n],atuple[x],atuple[y])
    return ()
print(triplet((-8, 0, 4, -2, -1, 1, 2)))