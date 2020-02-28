n1,n2=input("Enter 2 numbers separated with a single space: ").split(" ")
n1 = int(n1)
n2 = int(n2)
int (n1), int (n2)
prime_numbers = ""
for numero in range (n1 , n2+1):
    count = 0
    for number in range (1,numero+1):
        if numero%number==0:
            count += 1
    if count == 2:
        prime_numbers = prime_numbers + str(numero) + " "
print ("Prime numbers between %d and %d are: " %(n1,n2) + prime_numbers)