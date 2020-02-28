def odd_range(start, stop, step):
    if start%2==0:
        start+=1
    x=start
    while x<=stop:
        yield x
        x+=2*step
