def local_minima(alist, n):
    n = n//2
    out = []
    temp = []
    for i, num in enumerate(alist):
        if i - n < 0:
            temp = alist[:i+n+1]
            if num == min(temp):
                out.append((num,i))
        else:
            test = alist[i-n:i+n+1]
            if num == min(test):
                out.append((num,i))
    index=0
    while True:
        if out[index][0]==out[index+1][0] and out[index+1][1] <= out[index][1] + n:
            out.remove(out[index+1])
        if out[index][0]!=out[index+1][0]:
            index+=1
        if index >= len(out)-2:
            break
    return out