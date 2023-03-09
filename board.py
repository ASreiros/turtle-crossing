from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.draw_road()
        self.draw_line()

    def draw_road(self):
        self.penup()
        self.goto(-300, 0)
        self.pendown()
        self.pensize(500)
        self.color("dark gray")
        self.forward(600)

    def draw_line(self):
        self.penup()
        self.goto(-300, 0)
        self.color("white")
        self.width(2)

        for n in range(int(600 / 30)):
            if n % 2 == 0:
                self.pendown()
                self.forward(30)
            else:
                self.penup()
                self.forward(30)
