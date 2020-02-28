def greatest(num):
    num = str(num)
    num = sorted(num, reverse=True)
    out=""
    for elem in num:
        out+=elem
    out = int(out)
    return out