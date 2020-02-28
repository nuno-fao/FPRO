def recursive_dot(l1, l2):
    soma=0
    for i,elem in enumerate(l1):
        if type(elem)==list:
            soma += recursive_dot(l1[i],l2[i])
        else:
            soma+= l1[i]*l2[i]
    return soma