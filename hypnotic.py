import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.width(2)
t.hideturtle()


hue = 0
n = 360

for i in range(n):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)
    t.forward(i * 0.5)
    t.right(61)
    hue += 1/n

turtle.done()