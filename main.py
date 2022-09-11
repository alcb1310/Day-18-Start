import turtle
import turtle as t
import random

tim = t.Turtle()
tim.pensize(10)
tim.speed("fastest")

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
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
    random_color()
    tim.fd(travel_distance)

# Has to happen after all the code
screen = t.Screen()
screen.exitonclick()
