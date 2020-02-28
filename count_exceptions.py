def count_exceptions(f, n1, n2):
    out = 0
    for n in range(n1,n2+1):
        try:
            f(n)
        except:
            out+=1
    return out