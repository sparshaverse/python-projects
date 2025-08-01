import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red", "blue", "green", "purple", "orange", "yellow"]
t.hideturtle()

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)

turtle.done()