import turtle
t = turtle.Turtle()
colors = ['red', 'green', 'blue', 'yellow', 'purple']

t.speed(10)

for i in range(100):
    t.color(colors[i % 5])
    t.forward(i * 2)
    t.left(59)

turtle.done()