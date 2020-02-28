def parse(filename):
    f = open(filename)
    out=""
    lines=f.readlines()
    for i in range(len(lines)):
        lines[i]= "".join(lines[i].split())
        lines[i]=lines[i].strip("\n")
    for elem in lines:
        if elem == "(":
            out+=elem
        else:
            out+=elem + ","
    return eval("("+out+")")