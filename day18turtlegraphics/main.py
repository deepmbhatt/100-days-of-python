from turtle import Turtle, Screen,colormode
import random
tim = Turtle()
colormode(255)
def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    randomcolor = (r,g,b)
    return randomcolor
tim.pensize(10)
for i in range(3,11):
    degree = 360/i
    for j in range(0,i):
        tim.forward(100)
        tim.right(degree)
    tim.color(randomcolor())
        
    
    


screen = Screen()
screen.exitonclick()
