def override(l1, l2):
    over = []
    out = []
    for elem in l2:
        over.append(elem[0])
        out.append(elem)
    for elem in l1:
        if elem[0] not in over:
            out.append(elem)
    out.sort(key=lambda x: x[0])
    return out