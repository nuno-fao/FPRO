def inner(u,v):
    out = 0
    if len(u)==0:
        return 0
    for i in range(len(u)):
        out += u[i] * v[i]
    return out
print(inner([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]))