import random
num = int (input ("Provide an integer to find its square root: "))
x = random.randint(1,num)
while True:
    x1 = (x+num/x)/2
    if round(x1,2)==round(x,2):
        break
    x = x1
print(x1)