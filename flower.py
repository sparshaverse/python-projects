import turtle

t = turtle.Turtle()
t.speed(0)
t.color("red")
t.hideturtle()

for i in range(50):
    t.forward(100)
    t.left(123)
    t.forward(100)
    t.left(123)

turtle.done()