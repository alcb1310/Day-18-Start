from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.fillcolor("PaleGreen4")
tim.pencolor("PaleGreen4")

# or _ in range(4):
#    side_size = 50
#    tim.fd(side_size)
#    tim.rt(90)

# dash_size = 10
# for _ in range(15):
#     tim.pd()
#     tim.fd(dash_size)
#     tim.pu()
#     tim.fd(dash_size)

line_length = 100
for sides in range(3, 11):
    angle = 360 / sides
    for _ in range(sides):
        tim.fd(line_length)
        tim.rt(angle)

# Has to happen after all the code
screen = Screen()
screen.exitonclick()
