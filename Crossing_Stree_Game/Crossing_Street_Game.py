import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    scoreboard.difficulty()
    car.create_car()
    car.move()

    #Detecting collision with cars.
    for carro in car.all_cars:
        if abs(carro.xcor() - player.xcor()) < 27 and abs(carro.ycor() - player.ycor()) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detecting successful crossing
    if player.ycor() >= 280:
        player.reset_position()
        scoreboard.level_up()
        scoreboard.increse_difficulty()

screen.exitonclick()





