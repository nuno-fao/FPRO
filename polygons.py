import turtle
bicho = turtle.Turtle ()
sc = turtle.Screen ()
bicho.penup ()
bicho.forward(250)
for n in [3,4,6,8]:
    bicho.setheading(0)
    for _ in range(n):
        bicho.pendown ()
        bicho.fd(70)
        bicho.lt(360/n)
    bicho.penup ()
    bicho.setheading(180)
    bicho.forward(170)
sc.exitonclick ()
turtle.bye ()