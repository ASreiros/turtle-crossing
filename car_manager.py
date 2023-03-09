from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.moving_speed = STARTING_MOVE_DISTANCE
        self.timer = 0
        self.generate_cars()

    def create_car(self):
        if self.timer == 0:
            self.timer = 3
            car = Turtle("square")
            append_flag = False
            car.penup()
            car.color(random.choice(COLORS))
            coin = random.randint(0, 1)
            car.shapesize(stretch_wid=1, stretch_len=2)
            if coin:
                car_y = random.randint(10, 240)
                car_x = 300
                car.setheading(180)
            else:
                car_y = random.randint(-240, -10)
                car_x = -300
                car.setheading(0)
            car.goto(car_x, car_y)
            if self.collision(car):
                self.cars.append(car)
            else:
                car.goto(car_x, car_y + 20)
                self.cars.append(car)
        else:
            self.timer -= 1

    def generate_cars(self):
        probability = random.randint(1, 10)
        if probability >= 5:
            nr_of_cars = random.randint(1, 1)
            for n in range(nr_of_cars):
                self.create_car()

    def move_cars(self):
        new_cars = []
        for car in self.cars:
            car.forward(self.moving_speed)
            if 330 > car.xcor() > -330:
                new_cars.append(car)
        self.cars = new_cars

    def collision(self, t):
        flag = True
        t_ycor = t.ycor()
        for car in self.cars:
            if car.distance(t) < 25 and t_ycor+15 > car.ycor() > t_ycor-15:
                flag = False
        return flag

    def speed_up(self):
        self.moving_speed += MOVE_INCREMENT
