def exactly(s):
    t="123456789"
    out = ()
    for i,char in enumerate(s):
        for i2 in range(i+1,len(s)):
            print(x)
            if char in t and s[i+1] in t:
                if int(char)+int(s[2])==10:
                    x = s[i:i2].count("?")
                    if x==3:
                        out+=(char+s[i2],)
                    else:
                        return "no"
    return out
print(exactly("acc?7??sss?3rr1??????5???5"))