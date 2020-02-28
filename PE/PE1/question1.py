def fds(x,y):
    return 1000*(1+x/y)**y
r1 = int(input("First interest rate in percentage: "))/100
f1 = int(input("First payment frequency: "))
r2 = int(input("Second interest rate in percentage: "))/100
f2 = int(input("Second payment frequency: "))
print ("For r=%d and n=%d you'll have " %(r1,f1)+ str(fds(r1,f1)))
print ("For r=%d and n=%d you'll have " %(r2,f2)+ str(fds(r2,f2)))