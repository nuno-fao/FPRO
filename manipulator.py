def manipulator(l,cmds):
    out=""
    for cmd in cmds:
        cmd = cmd.split()
        if cmd[0]=="insert":
            l.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0]=="print":
            out += " " + str(l)
        elif cmd[0]=="remove":
            l.remove(int(cmd[1]))
        elif cmd[0]=="append":
            l.append(int(cmd[1]))
        elif cmd[0]=="sort":
            l.sort()
        elif cmd[0]=="pop":
            l=l[:-1]
        elif cmd[0]=="reverse":
            l=l[::-1]
    return out