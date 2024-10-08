from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200, 260)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Refresh scoreboard"""
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def game_over(self):
        """Display GAME OVER"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def increase_level(self):
        """Increase level count on scoreboard"""
        self.level += 1
