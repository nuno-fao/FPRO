def isomorphic(astring1, astring2):
    transf = {}
    out = []
    for i,elem in enumerate(astring1):
        if elem not in transf:
            if astring2[i] not in transf.values():
                transf[elem]=astring2[i]
            else:
                return "'{}' and '{}' are not isomorphic".format(astring1,astring2)
        elif elem in transf and transf[elem]!=astring2[i]:
            return "'{}' and '{}' are not isomorphic".format(astring1,astring2)
    for key, value in transf.items():
        out.append((key,value))
    return "'{}' and '{}' are isomorphic because we can map: {}".format(astring1,astring2,out)