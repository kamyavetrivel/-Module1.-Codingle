import turtle


screen = turtle.Screen()
screen.bgcolor("orange")

t = turtle.Turtle()
t.color("purple")
t.speed(3)


for i in range(6):
    t.forward(80)
    t.left(60)

turtle.done()

