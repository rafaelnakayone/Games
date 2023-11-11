from turtle import Turtle
import time

FONT = ("Courier", 16, "normal")
ALIGN = "center"
DECREASE_TIME = 0.025


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 1
        self.refresh_level()
        self.time_sleep = 0.2

    def refresh_level(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level:{self.level}", False, ALIGN, FONT)

    def level_up(self):
        self.level += 1
        self.refresh_level()

    def difficulty(self):
        time.sleep(self.time_sleep)

    def increse_difficulty(self):
        self.time_sleep -= DECREASE_TIME

    def game_over(self):
        self.home()
        self.write("GAME OVER.", False, ALIGN, ("Courier", 28, "normal"))



