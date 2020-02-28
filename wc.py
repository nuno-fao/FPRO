def wc(filename):
    file=open(filename)
    lines,words,char=0,0,0
    while True:
        cur_line=file.readline()
        if len(cur_line)==0:
            break
        lines+=1
        words+=len(cur_line.split())
        char+=len(cur_line)
    file.close()
    return (lines,words,char)