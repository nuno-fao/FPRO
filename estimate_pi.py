import random
import statistics
import math
n = 0                                           #variable for doubling the number of needles if needed
while True:                                     #do it forever until the condition for "break" is met
    all_pi = []                                 #list that will hold all the calculations of pi
    total_needles=1000*(2**n)
    for _ in range (100):                       #number of pi estimations per list
        inside = 0                              #declaring and resetting the number of needles inside
        for _ in range (total_needles):         #throw needles as many times in toal_needles
            x = random.random()**2              #mathematical equation of the circle
            y = random.random()**2
            if math.sqrt(x+y)<1.0:              #the radius is 1 so if this equation is false the needle fell out of the circle
                inside+=1   
        pi =  (4 * inside) / total_needles
        all_pi.append(pi)                       #add this value of pi to the list of 100
    z = statistics.stdev(all_pi)
    print("The average of pi with", total_needles, "needles is", sum(all_pi)/len(all_pi))
    print("As for the standart deviation, it is:", z, "\n")
    n+=1                                        #increment n to double the total number of needles
    if z<=0.005:
        break