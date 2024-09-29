import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cars = []


def create_car():
    """Create car"""
    new_car = CarManager()
    new_car.car_speed = car_manager.car_speed
    cars.append(new_car)


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
player = Player()
car_manager = CarManager()
car_manager.hideturtle()
scoreboard = Scoreboard()

screen.onkey(player.move_forward, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()

    if random.randint(1, 6) == 1:
        create_car()

    for car in cars:
        car.car_move()

    for car in cars:
        if car.xcor() < -320:
            cars.remove(car)

    for car in cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 275:
        scoreboard.increase_level()
        player.reset_position()

        for car in cars:
            car.hideturtle()
            car.clear()
        cars.clear()

        car_manager.increase_speed()

screen.exitonclick()
