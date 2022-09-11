from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.fillcolor("PaleGreen4")
timmy_the_turtle.pencolor("PaleGreen4")
timmy_the_turtle.fd(100)
timmy_the_turtle.rt(90)

# Has to happen after all the code
screen = Screen()
screen.exitonclick()
