import datetime
x = datetime.datetime.now().hour
y = datetime.datetime.now().minute
print ("Now: " + str(x) + ":" +str(y))
x+=8
y+=30
if y>=60:
    y-=60
    x+=1
if x >= 24:
    x-=24
print ("Alarm: " + str(x).zfill(2) + ":" +str(y).zfill(2))