from turtle import Turtle, Screen

side_size = 50
tim = Turtle()
tim.shape("turtle")
tim.fillcolor("PaleGreen4")
tim.pencolor("PaleGreen4")

for _ in range(4):
    tim.fd(side_size)
    tim.rt(90)

# Has to happen after all the code
screen = Screen()
screen.exitonclick()
