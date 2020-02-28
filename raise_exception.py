def raise_exception(alist, value):
    out=[]
    for elem in alist:
        if elem <= value:
            out.append(ValueError("{} is not greater than {}".format(elem,value)))
    return out