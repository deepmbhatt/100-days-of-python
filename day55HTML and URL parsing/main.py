from flask import Flask, render_template
import requests
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

@app.route('/')
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjhscHdweXoxenBqeHlpc25mbXE4dWM5YmVmaXhrNHhhNHc2aXNkdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IsfrRWvbUdRny/giphy.gif'/>")

@app.route('/<int:num>')
def check_number(num):
    if random_number == num:
        return ("<h1 style='color:green'>You found me!</h1>"
                "<img src='https://media.giphy.com/media/2m1lj8p8v6JcWpREtL/giphy.gif?cid=790b7611d0l1th3jyqn5x8ziwypfewoztwah53gurf55q1nu&ep=v1_gifs_search&rid=giphy.gif&ct=g'/>")
    elif random_number < num:
        return ("<h1 style='color:red'>Too high, try again!</h1>"
                "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWwzZDJub2I0MGxtd3piMGRkYXUyNnNsbXN3aDJiejBiOHl4ZGZxMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3BRDkVjKikYW4/giphy.gif'/>")
    else:
        return ("<h1 style='color:purple'>Too low, try again!</h1>"
                "<img src='https://media.giphy.com/media/cTQ3rS603cuvwnMHTb/giphy.gif?cid=790b7611wdfrrnv4hu1yrgcj21ewfjd6xokzole1xy76ege6&ep=v1_gifs_search&rid=giphy.gif&ct=g'/>")
if __name__ == "__main__":
    app.run(debug=True)
