from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move_forward(self):
        """Move player turtle"""
        self.fd(10)

    def reset_position(self):
        """Go back turtle to starting position"""
        self.goto(STARTING_POSITION)
