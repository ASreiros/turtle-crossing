import turtle
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.level_up()

    def level_up(self):
        self.clear()
        self.level += 1
        self.goto(-200, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.penup()
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        self.goto(0, -50)
        self.write(f"You reached {self.level} level", align="center", font=FONT)


