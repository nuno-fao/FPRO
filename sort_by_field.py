def sort_by_field(filename, field):
    f = open(filename)
    out=[]
    out2=""
    while True:
        c=f.readline()
        if len(c)==0:
            break        
        c=c.strip("\n")
        u=c.split(",")
        out.append(u)
    pos=out[0].index(field)
    temp=out[0]
    out=out[1:]
    out=sorted(out, key=lambda x: x[pos])
    out=[temp]+out
    for elem in out:
        out2+=",".join(elem)
        out2+="\n"
    return out2