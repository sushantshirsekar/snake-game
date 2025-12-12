from turtle import Turtle

# Constants
FONT = ("courier", 20, "bold")
ALIGNMENT = "center"
MOVE = False

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", move=MOVE, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}", move=MOVE, align=ALIGNMENT, font=FONT)

