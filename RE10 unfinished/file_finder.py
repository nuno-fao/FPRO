def file_finder(dirs, file_name):
    for direct in dirs[1:]:
        if file_name==direct:
            return "{}/{}".format(dirs[0],direct)
        else:
            if type(direct)==list:
                out = file_finder(direct, file_name)
                if out!=None:
                    return "{}/{}".format(dirs[0],out)