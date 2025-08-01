import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("A man passing by a house")

house = turtle.Turtle()
house.speed(0)
house.penup()
house.goto(-100, -50)
house.pendown()
house.color("brown")
house.begin_fill()
for _ in range(4):
    house.forward(100)
    house.left(90)
    house.end_fill()


house.color("red")
house.begin_fill()
house.goto(-100, 50)
house.goto(50, -100)
house.goto(0, 50)
house.goto(-100, 50)
house.end_fill()
house.hideturtle()

man = turtle.Turtle()
man.speed(1)
man.color("black")
man.penup()
man.goto(-200, -50)


def draw_man(x, y):
    man.clear()
    man.penup()
    man.goto(x, y)
    man.pendown()

    man.circle(5)

    man.right(90)
    man.forward(15)

    man.left(30)
    man.forward(10)
    man.backward(10)
    man.right(60)
    man.forward(10)
    man.backward(10)
    man.left(30)

    man.forward(10)
    man.left(30)
    man.forward(10)
    man.backward(10)
    man.right(60)
    man.forward(10)
    man.penup()
    man.setheading(0)


x = -200
while x < 150:
    draw_man(x, -40)
    x += 5

turtle.done()
    

