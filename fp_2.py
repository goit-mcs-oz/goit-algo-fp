# Завдання 2

import turtle


def pythagoras_curve(t, order, size):
    if order == 0:
        return

    t.forward(size/1.45)

    t.left(45)
    pythagoras_curve(t, order - 1, size/1.45)
    t.right(45)

    t.right(45)
    pythagoras_curve(t, order - 1, size/1.45)
    t.left(45)

    t.backward(size/1.45)


def draw_pythagoras_tree(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0,  - size)
    t.pendown()
    t.left(90)

    pythagoras_curve(t, order, size)
    window.mainloop()


draw_pythagoras_tree(8)
