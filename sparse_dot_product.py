def sparse_dot_product(dict1, dict2):
    out = 0
    for i in dict1.keys():
        if i in dict2:
            out += dict1[i] * dict2[i]
    return out