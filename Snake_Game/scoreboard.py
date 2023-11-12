from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)
        self.goto(0, -20)
        self.write(f" FINAL SCORE: {self.score}", False, ALIGNMENT, FONT)

