from painting import rgb_colors
import random
from turtle import Turtle, Screen, colormode
colormode(255)
tim = Turtle()
dots=100
tim.penup()
tim.hideturtle()
for i in range(1,dots+1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    if i%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(360)


screen = Screen()
screen.exitonclick()
