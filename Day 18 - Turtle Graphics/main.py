from turtle import Turtle, Screen
import random

colors = ["white smoke", "dark green", "olive drab", "dark red", "orange", "indigo", "indian red", "dark cyan"]
timmy = Turtle()
timmy.shape("turtle")
timmy.penup()
timmy.goto(-50, 200)
timmy.pendown()

for i in range(3, 16):
    timmy.color(random.choice(colors))
    for j in range(i):
        timmy.pendown()
        timmy.forward(100)
        timmy.right(360/i)


screen = Screen()
screen.exitonclick()
