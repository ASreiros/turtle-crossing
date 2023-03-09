import time
from turtle import Screen
from board import Board
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("light green")
screen.tracer(0)

scoreboard = Scoreboard()
board = Board()
player = Player()
manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    manager.move_cars()
    manager.generate_cars()
    if not manager.collision(player):
        scoreboard.game_over()
        game_is_on = False
    elif player.ycor() > 255:
        player.start()
        scoreboard.level_up()
        manager.speed_up()

screen.exitonclick()
