from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(20)


def move_backward():
    timmy.backward(20)


def move_c_clockwise():
    timmy.left(10)


def move_clockwise():
    timmy.right(10)


def clear_screen():
    screen.resetscreen()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_c_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear_screen, "c")


screen.exitonclick()
