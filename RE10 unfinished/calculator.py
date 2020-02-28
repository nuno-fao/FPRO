def calculator(expr):
    if type(expr)==int:
        return expr
    if type(expr[0])==tuple:
        expr = (calculator(expr[0]),)+expr[1:]
    if type(expr[2])==tuple:
        expr = expr[:2] + (calculator(expr[2]),)
    if type(expr[0])==int and type(expr[2])==int:
        if expr[1]=="+":
            expr = expr[0] + expr[2]
        elif expr[1]=="-":
            expr = expr[0] - expr[2]
        else:
            expr = expr[0] * expr[2]        
    return expr