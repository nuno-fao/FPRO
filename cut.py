def cut(filename, delimiter, field):
    file=open(filename)
    lines=file.readlines()
    out=""
    for line in lines:
        line=line.strip("\n")
        line=line.split(delimiter)
        if type(field)==int:
            out+=line[field-1]+delimiter
        else:
            for elem in field:
                out+=line[elem-1]+delimiter
        out=out[:-1]+"\n"
    file.close()
    return out