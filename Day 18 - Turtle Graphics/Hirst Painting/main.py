import colorgram
import turtle as t
import random

colors = colorgram.extract('image.jpg', 30)

#
# COMPUTATION TO EXTRACT COLORS FROM JPG IMAGE
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(219, 231, 240), (241, 222, 231), (121, 169, 196), (222, 238, 230), (54, 104, 143), (190, 143, 165),
              (145, 65, 92), (130, 179, 158), (226, 201, 120), (57, 124, 89), (150, 84, 60), (165, 164, 56),
              (193, 84, 110), (217, 87, 62), (133, 32, 52), (76, 161, 130), (225, 170, 189), (55, 162, 184),
              (69, 33, 53), (237, 169, 157), (151, 213, 200), (108, 119, 171), (43, 56, 108), (34, 44, 72),
              (145, 210, 222), (71, 39, 27), (180, 185, 216), (123, 38, 30)]
screen = t.Screen()
screen.screensize(15, 15)
screen.setworldcoordinates(-1, -1, 10, 10)

timmy = t.Turtle()
t.colormode(255)

i = j = 0
while i < 10:
    while j < 10:
        timmy.setx(j)
        timmy.pendown()
        timmy.color(random.choice(color_list))
        timmy.dot(35)
        timmy.penup()
        j += 1
    timmy.penup()
    i += 1
    timmy.sety(i)
    j = 0

timmy.hideturtle()
screen.exitonclick()