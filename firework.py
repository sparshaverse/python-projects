import turtle
import random


screen = turtle.Screen()
screen.bgcolor("black")


t = turtle.Turtle()
t.speed(0)
t.hideturtle()

colors = ["red", "green", "blue", "yellow", "purple", "orange"]

def firework(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(random.choice(colors))
    for i in range(36):
        t.forward(50)
        t.backward(50)
        t.right(10)


screen.onscreenclick(firework)


turtle.mainloop()


