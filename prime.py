result = int(input("Write an integer and i'll check if it is a prime: "))
divisores = 0
for n in range (1, result+1):
    if result % n == 0:
        divisores += 1
if divisores == 2:
    result = True
else: 
    result = False