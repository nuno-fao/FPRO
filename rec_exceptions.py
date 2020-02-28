def rec_exceptions(l):
    out=[]
    for elem in l:
        try:
            elem()
        except Exception as exc:
            out.append(exc)
        else:
            out += rec_exceptions(elem())
    return out
print(rec_exceptions([lambda: [lambda: [1,2,3].index(-1), lambda: ''[2]], lambda: [1,2,3][4], lambda: [lambda: [lambda: 1/0]]]))