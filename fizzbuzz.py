result = ""
numbers = []
n = 0
num = int(input("Provide an integer to play FizzBuzz: "))
for _ in range (num):
    n += 1
    numbers.append (n)
for number in (numbers):
    if (number) % 3 == 0 and number % 5 == 0:
        continue
    elif number % 3==0:
        result = result + "Fizz "
    elif number % 5==0:
        result = result + "Buzz "
    else:
        result = result + str(number) + " "
print (result)