def palindrome(astring):
    out = 0
    for i in range(len(astring)-1):
        for i2 in range(i+1,len(astring)):
            temp = astring[i]+astring[i+1:i2+1]
            if temp==temp[::-1]:
                out += 1
    return out