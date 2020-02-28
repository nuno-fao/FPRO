def evaluate(a, x):
    y=[elem*x**i for i,elem in enumerate(a)]
    return sum(y)