out = []
def flatten(alist):
    for elem in alist:
        if type(elem)==list:
            flatten(elem)
        else:
            out.append(elem)
    return out