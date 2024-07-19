from turtle import Turtle

# Define starting positions for the snake segments
STARTING_POSITIONs = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20  # Distance to move the snake forward
UP = 90  # Angle to move the snake up
DOWN = 270  # Angle to move the snake down
RIGHT = 0  # Angle to move the snake right
LEFT = 180  # Angle to move the snake left

class Snake:
    # Initialize the Snake object
    def __init__(self):
        self.segments = []  # List to store segments of the snake
        self.create_snake()  # Call the method to create the snake
        self.head = self.segments[0]

    # Method to create the snake at the starting positions
    def create_snake(self):
        for position in STARTING_POSITIONs:  # Loop through each starting position
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")  # Create a turtle object for each segment
        new_segment.color("white")  # Set the color of the segment
        new_segment.penup()  # Lift the pen to move the turtle without drawing
        new_segment.goto(position)  # Move the turtle to the starting position
        self.segments.append(new_segment)  # Add the segment to the list of segments

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Method to move the snake forward
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Start from the last segment and move towards the first
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the segment ahead
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the segment ahead
            self.segments[seg_num].goto(new_x, new_y)  # Move the current segment to the position of the segment ahead
        self.segments[0].forward(MOVE_DISTANCE)  # Move the first segment forward by 20 units

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
