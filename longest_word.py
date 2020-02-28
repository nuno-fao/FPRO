def longest_word(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    dic={}
    f = open("words")
    while True:
        c=f.readline() 
        if len(c)==0:
            break
        if type(c)!=type("yre"):
            c=str(c)
        if c in dic:
            dic[c[:-1]]+=1
        else:
            dic[c[:-1]]=1
    lista=html.split(" ")
    keys = set(lista).intersection(set(dic.keys()))
    fin=sorted([l for l in keys], key=lambda x: len(x),reverse=True)
    out=[]
    length=len(fin[0])
    for c in fin:
        if len(c)==length:
            out.append(c)
    out.sort()
    return out[0]
