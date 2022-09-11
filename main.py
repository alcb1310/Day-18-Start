import turtle
import turtle as t
import random

tim = t.Turtle()
# tim.pensize(1)
tim.speed("fastest")

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor(r, g, b)


angle = 0
step = 3
for _ in range(0, 360, step):
    random_color()
    tim.circle(80)
    angle += step
    tim.setheading(angle)

# Has to happen after all the code
screen = t.Screen()
screen.exitonclick()
