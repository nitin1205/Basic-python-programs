import turtle
import random

screen = turtle.Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color:- ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = -100
for i in range(6):
    a = turtle.Turtle(shape = "turtle")
    a.color(colors[i])
    a.penup()
    a.goto(x = -230, y = y)
    y += 45
    all_turtles.append(a)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            winningh_color = turtle.pencolor()
            if winningh_color == user_bet:
                print("You Won!!!")
            else:
                print("You Lose!!!")
            is_race_on = False
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

   
screen.exitonclick()