from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class StatesOnMap(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.x_cor = 0
        self.y_cor = 0

    def try_again(self):
        self.write("Incorrect answer!\nTry again!", False, ALIGNMENT, FONT)
