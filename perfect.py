def is_perfect(n):
    divisores = []
    for number in range(1,n):
        if n%number==0:
            divisores.append(number)
    if sum(divisores)==n:
        return True
    if sum(divisores)!=n:
        return False