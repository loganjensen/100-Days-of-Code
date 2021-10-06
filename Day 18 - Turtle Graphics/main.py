from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.penup()
timmy.goto(-50, 200)
timmy.pendown()

for i in range(3, 15):
    for j in range(i):
        timmy.pendown()
        timmy.forward(100)
        timmy.right(360/i)


screen = Screen()
screen.exitonclick()
