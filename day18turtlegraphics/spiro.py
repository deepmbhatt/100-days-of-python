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
tim.speed("fastest")
def draw_spiro(size):
    for _ in range(int(360/size)):
        tim.color(randomcolor())
        tim.circle(100)
        tim.setheading(tim.heading() + size)

draw_spiro(5)
screen = turtle.Screen()
screen.exitonclick()
