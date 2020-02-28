def map(pos,steps):
    steps = steps.split("-")
    x=pos[0]
    y=pos[1]
    for elem in steps:
        if elem=="up":
            y+=1
        elif elem=="down":
            y-=1
        elif elem=="right":
            x+=1
        elif elem=="left":
            x-=1
    return (x,y)