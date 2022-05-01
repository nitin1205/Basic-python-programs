import turtle 
import random

def random_color():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    rc = (r, g, b)
    return rc

"""
turtle.colormode(255)
direction = [0,90,180,270]
a=turtle.Turtle()
a.width(4)
a.speed("fast")


for i in range(200):
    a.pencolor(random_color())
    a.forward(20)
    a.setheading(random.choice(direction))
"""

def draw_spiral(size_of_gap):
    for i in range(int(360/size_of_gap)):
        a.pencolor(random_color())
        a.circle(100)
        a.seth(a.heading() + size_of_gap)


a=turtle.Turtle()
a.width(2)
turtle.colormode(255)
a.speed("fastest")

draw_spiral(5)