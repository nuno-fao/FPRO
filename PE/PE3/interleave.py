def interleave(alist1, alist2):
    out2=[]
    if len(alist1)<=len(alist2):
        for i2,elem2 in enumerate(alist1):
            if type(elem2)==list:
                out2+=connect(alist1[i2],alist2[i2])
            else:
                out2+=[alist1[i2],alist2[i2]]
    else:
        for i2,elem2 in enumerate(alist2):
            if type(elem2)==list:
                out2+=connect(alist1[i2],alist2[i2])
            else:
                out2+=[alist1[i2],alist2[i2]]
    return out2
def connect(l1,l2):
    out=[]
    if len(l1)<=len(l2):
        for i,elem in enumerate(l1):
            out.append(l1[i])
            out.append(l2[i])
    else:
        for i,elem in enumerate(l2):
            out.append(l1[i])
            out.append(l2[i])
    return out