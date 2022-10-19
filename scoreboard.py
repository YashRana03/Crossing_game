from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")


# ScoreBoard class creates the scoreboard object
class ScoreBoard(Turtle):
    # Creates scoreboard from turtle class
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto(-200, 250)
        self.write(arg=f"Level {self.level + 1}", align="center", font=FONT)

    # Displays the "go!" instruction on the screen and then displays the level
    def go(self):
        self.goto(0, 0)
        self.write(arg="GO!", align="center", font=FONT)
        time.sleep(1)
        self.clear()
        self.print_level()

    # Displays the level of the player on the screen
    def print_level(self):
        self.goto(-200, 250)
        self.write(arg=f"Level {self.level + 1}", align="center", font=FONT)

    # Displays "Game Over on the screen"
    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(arg=f"Game over", align="center", font=FONT)

    # Updates the game level on the screen
    def update_level(self):
        self.clear()
        self.goto(-200, 250)
        self.level += 1
        self.write(arg=f"Level {self.level + 1}", align="center", font=FONT)

    # Returns the current game level
    def get_level(self):
        return self.level


