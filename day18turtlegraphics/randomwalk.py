import turtle
import random
directions=[0, 90, 180 ,270]
tim = turtle.Turtle()
turtle.colormode(255)
def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    randomcolor = (r,g,b)
    return randomcolor
tim.pensize(10)
tim.speed("fastest")
for i in range(0,200):
    tim.forward(20)
    tim.setheading(random.choice(directions))
    tim.color(randomcolor())
screen = turtle.Screen()
screen.exitonclick()
