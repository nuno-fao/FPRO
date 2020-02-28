def anagrams(alist):
    temp = []
    out=[]
    for elem in alist:
        elem = "".join(elem.split())
        sort = "".join(sorted(elem.lower()))
        temp.append(sort)
    for i,coiso in enumerate(temp):
        nested=[alist[i]]
        for i2 in range(len(temp)):
            if coiso==temp[i2] and i!=i2:
                nested.append(alist[i2])
        nested.sort()
        if nested not in out:
            out.append(nested)
    out = sorted(out, key=lambda x: x[0].lower())
    return out