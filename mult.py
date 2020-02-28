def mult(M,N):
    if len(M[0])!=len(N):
        return []
    else:
        out = []
        for c in range (len(M)):
            out.append([])
            for l in range(len(N[0])):
                temp=0
                for x in range (len(M[0])):
                    temp += M[c][x] * N[x][l]
                out[c].append(temp)
    return out