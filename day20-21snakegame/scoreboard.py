from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.score = 0  # Initialize the score to 0
        self.color("white")
        self.penup()    # Lift the pen to move the turtle without drawing
        self.goto(0, 270)  # Move the turtle to the top of the screen
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal")) # Write the initial score on the screen
        self.hideturtle()  # Hide the turtle cursor

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)  # Update the score on the scree
    
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()  # Call the method to update the score on the screen

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)  # Write "GAME OVER" on the screen
        
        