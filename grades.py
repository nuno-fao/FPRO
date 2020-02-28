def sort_grades(records):
    records = sorted(records, key=lambda x: x[0]+x[1][2:])
    records = sorted(records, key=lambda x: sum(x[2])/len(x[2]), reverse=True)
    records = tuple(records)       
    return records