#function file #debiaowufunctions
import turtle
bob=turtle.Turtle()


def polygon(sides,distance,color):
    angle = 360/sides
    bob.color(color)
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
    bob.end_fill()

def jump(x,y):
    bob.pu()
    bob.goto(x,y)
    bob.pd()

def star(d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(5):
        bob.forward(d)
        bob.left(144)
    bob.end_fill()

def explosion(d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(d)
        bob.right(135)
    bob.end_fill()
