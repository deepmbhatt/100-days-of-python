import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
#screen.setup(width=725, height=491)
image = "day25usstatequiz/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.bgpic(image)



data = pd.read_csv("day25usstatequiz/50_states.csv")
all_states = data["state"].to_list()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

#if answer_state in data["state"].to_list():
if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x.item()), int(state_data.y.item()))
    t.write(answer_state)
    all_states.remove(answer_state)

    while len(all_states) > 0:
        answer_state = screen.textinput(title=f"{len(all_states)} States Remaining", prompt="What's another state's name?").title()
        if answer_state == "Exit":
            break
        if answer_state in all_states:
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
            all_states.remove(answer_state)

screen.exitonclick()


