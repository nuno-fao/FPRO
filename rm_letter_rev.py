def rm_letter_rev(l, astr):
    i=""
    for x in astr:
        if l!=x:
            i+=x
    return i[::-1]