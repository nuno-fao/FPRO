def collisions(alist):
    out = {}
    for elem in alist:
        partial = 0
        for char in str(elem):
            partial += int(char)
        key = partial % 8
        if key in out:
            out[key]+=1
        else:
            out[key]=1
    return out