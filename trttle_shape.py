import random
import turtle as t
color = ["white smoke", "light gray", "dark gray", "light slate gray", "light steel blue", "cornflower blue", "medium blue", "deep sky blue", "powder blue", "sky blue",
        "steel blue", "cyan", "pale turquoise", "cadet blue", "dark cyan", "dark slate gray", "dark sea green", "dark orchid", "purple", "indigo", "medium violet red",
        "sandy brown", "magenta", "firebrick", "sienna", "forest green", "spring green", "lime", "yellow", "olive"]
a=t.Turtle()
a.width(4)
for i in range(3,11):
    a.color(random.choice(color))
    for j in range(i):
        a.forward(100)
        a.right(360/i)