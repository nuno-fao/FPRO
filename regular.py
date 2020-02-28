import turtle
bicho = turtle.Turtle ()
sc = turtle.Screen ()
n = int(input("How many sides will your polygon have? "))
color = bicho.color(input("What shall be the color of the border? "))
length = int(input("Length of each side? "))
bicho.fillcolor(input("How about the colour of the inside? "))
bicho.begin_fill()
for _ in range(n):
    bicho.fd(length)
    bicho.lt(360/n)
bicho.end_fill()
sc.exitonclick ()
turtle.bye ()