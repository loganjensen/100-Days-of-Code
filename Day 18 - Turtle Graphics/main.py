import turtle as t
import random


colors = ["dark green", "olive drab", "dark red", "orange", "indigo", "indian red", "dark cyan", "magenta", "navy", "powder blue"]
directions = [0, 90, 180, 270]

timmy = t.Turtle()
t.colormode(255)
timmy.pensize(1)
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


#
# DRAW POLYGONS
#
# for i in range(3, 16):
#     timmy.color(random.choice(colors))
#     for j in range(i):
#         timmy.pendown()
#         timmy.forward(100)
#         timmy.right(360/i)

#
# RANDOM WALK
#
# for _ in range(250):
#     timmy.color(random_color())
#     timmy.forward(20)
#     timmy.right(random.choice(directions))

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)

draw_spirograph(1)

screen = t.Screen()
screen.exitonclick()
