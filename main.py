import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.pensize(10)
tim.speed("fastest")

screen.colormode(255)


def select_color():
    r = random.randint(0, 254)
    g = random.randint(0, 254)
    b = random.randint(0, 254)
    tim.pencolor(r, g, b)


# coordinates = ["north", "east", "south", "west"]
direction = [0, 90, 180, 270]

#
# def turn_north():
#     while tim.heading() != 90:
#         tim.lt(90)
#
#
# def turn_east():
#     while tim.heading() != 0:
#         tim.lt(90)
#
#
# def turn_south():
#     while tim.heading() != 270:
#         tim.lt(90)
#
#
# def turn_west():
#     while tim.heading() != 180:
#         tim.lt(90)


travel_distance = 20
for _ in range(250):
    # direction = random.choice(coordinates)
    # if direction == "north":
    #     turn_north()
    # elif direction == "east":
    #     turn_east()
    # elif direction == "south":
    #     turn_south()
    # elif direction == "west":
    #     turn_west()
    tim.setheading(random.choice(direction))
    select_color()
    tim.fd(travel_distance)

# Has to happen after all the code
screen.exitonclick()
