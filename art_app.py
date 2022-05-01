import turtle



def move_forward():
    a.fd(10)

def move_backward():
    a.bk(10)    

def turn_right():
    x=a.heading() - 10
    a.setheading(x)

def turn_left():
    x=a.heading() + 10
    a.setheading(x)

def clear():
    a.clear()
    a.penup()
    a.home()
    a.pendown()

a=turtle.Turtle()
screen = turtle.Screen()


screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=clear)
screen.exitonclick()