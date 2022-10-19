import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

# Setting up the window
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = ScoreBoard()

num = 10
list_cars = []
incrementer = 6
game_is_on = True

while game_is_on:
    # Allows the user to play after a delay
    if num == 100:
        screen.onkeypress(player.move_up, "Up")
        scoreboard.go()

    # Creates a new car every after a certain number of iterations, which is updated at each level of the game
    if num % incrementer == 0:
        new_car = CarManager(player.get_random_pos(), scoreboard.get_level())
        list_cars.append(new_car)

    # Moves every car created forwards
    for car in list_cars:
        car.move_forward()

    # Checks if the turtle has it a car if so the game is ended
    for car in list_cars:
        y_distance = int((car.ycor() - player.ycor()))
        x_distance = int(abs(car.xcor() - player.xcor()))
        if y_distance > 0:
            if y_distance <= 25 and x_distance <= 33 and player.ycor() > -260:
                game_is_on = False
                scoreboard.game_over()
        else:
            if abs(y_distance) <= 20 and x_distance <= 33 and player.ycor() > -260:
                game_is_on = False
                scoreboard.game_over()

    # Checks if the player has reached the top in if so the new level is set
    if player.is_at_finish():
        scoreboard.update_level()
        player.reinitialize()
        for car in list_cars:
            car.increase_speed()
        if incrementer != 1:
            incrementer -= 1

    num += 1
    time.sleep(0.1)
    screen.update()

screen.exitonclick()

