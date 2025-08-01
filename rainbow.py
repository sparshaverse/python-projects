import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
t.hideturtle()


for radius in range(20, 200, 20):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.color(colors[radius % 6])
    t.circle(radius)

turtle.done()