from turtle import Turtle, Screen
import random
screen= Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You have won the bet! The {win_color} turtle is the winner!")
            else:
                print(f"You have lost the bet! The {win_color} turtle is the winner!")
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()