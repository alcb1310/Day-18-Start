from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.fillcolor("PaleGreen4")
tim.pencolor("PaleGreen4")

# or _ in range(4):
#    side_size = 50
#    tim.fd(side_size)
#    tim.rt(90)

dash_size = 5
for _ in range(50):
    tim.pd()
    tim.fd(dash_size)
    tim.pu()
    tim.fd(dash_size)

# Has to happen after all the code
screen = Screen()
screen.exitonclick()
