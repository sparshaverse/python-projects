from turtle import *
from colorsys import *
speed(0)
bgcolor("black")
c = 0
for i in range(100):
    c+=0.002
    color(hsv_to_rgb(c, 1, 1))
    circle(110, 270)
    penup()
    goto(0, i)
    pendown()
done()

