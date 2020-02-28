def find_dtype(atuple, data_type):
    new_tuple = ()
    for item in atuple:
        if type(item).__name__==data_type:
            new_tuple += (item,)
    return new_tuple