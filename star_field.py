import turtle
import random

turtle.bgcolor("black")
t = turtle.Turtle()
t.color("white")
t.speed(0)
t.hideturtle()


for _ in range(100):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.penup()
    t.goto(x,y)
    t.dot(random.randint(2, 5))


turtle.done()