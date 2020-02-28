def translate(astring, table):
    new_string = ""
    for element in astring:
        new_string += element
        for pair in table:
            if pair[0]==element:
                new_string = new_string[:-1]
                new_string += str(pair[1])
                break
    return new_string
print (translate("Hello world!",table=(('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5), ('!', ' :)'))))