starting_money = 1000
frequency = 2
interest_rate = 1/100
years = 2
print ("1.", starting_money*(1 + interest_rate/frequency)**(frequency*years))
starting_money = 650
frequency = 1
interest_rate = -0.05/100
print ("2.", starting_money*(1 + interest_rate/frequency)**(frequency*years))
starting_money = int(input("How much do you wish to invest? "))
frequency = int(input("Frequency of payment per year? "))
interest_rate = float(input("How about the percentage interest rate? "))/100
print ("3.", starting_money*(1 + interest_rate/frequency)**(frequency*years))