from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# Class CarManager creates the car object
class CarManager(Turtle):
    # Creates the car using the turtle class
    def __init__(self, pos, level):
        super().__init__()
        self.penup()
        self.goto(pos)
        self.color(choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2.5)
        self.moving_distance = STARTING_MOVE_DISTANCE + level*MOVE_INCREMENT

    # Moves the car to the left of the screen
    def move_forward(self):
        self.setheading(180)
        if self.xcor() > -1000:
            self.forward(self.moving_distance)

    # Increases the speed of the car
    def increase_speed(self):
        self.moving_distance += MOVE_INCREMENT

