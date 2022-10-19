from turtle import Turtle
from random import randint

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Player class creates the turtle avatar
class Player(Turtle):
    # Creates the turtle and sends it to the starting position on the screen
    def __init__(self):
        super().__init__()
        self.color("black")
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)

    # Returns a random position
    def get_random_pos(self):
        x_pos = randint(300, 301)
        y_pos = randint(-250, 280)
        pos = (x_pos, y_pos)
        return pos

    # Moves the turtle up
    def move_up(self):
        self.forward(10)

    # Resets the position of the turtle to the starting position
    def reinitialize(self):
        self.goto(STARTING_POSITION)

    # Checks to see if the user has reached the end of the current level
    def is_at_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
