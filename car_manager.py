from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(1, 2)
        self.penup()
        self.seth(180)
        rand_y = random.randint(-270, 270)
        rand_color = random.choice(COLORS)
        self.car_speed = STARTING_MOVE_DISTANCE
        self.color(rand_color)
        self.goto(300, rand_y)
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_move(self):
        """Move car"""
        self.forward(self.car_speed)

    def increase_speed(self):
        """Increase car speeed"""
        self.car_speed += MOVE_INCREMENT
