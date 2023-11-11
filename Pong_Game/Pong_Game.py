from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

initial_position = (350, 0)
initial_position2 = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(initial_position)
l_paddle = Paddle(initial_position2)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    #Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddles.
    if ball.distance(r_paddle) < 51 and ball.xcor() > 320 or ball.distance(l_paddle) < 51 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect left wins
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect right wins
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()











screen.exitonclick()