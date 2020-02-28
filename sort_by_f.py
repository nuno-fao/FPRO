def sort_by_f(l):
    l.sort(key=lambda x: x if x<5 else 5-x)
    return l
