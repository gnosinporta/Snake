from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0

        # creates the scoreboard and places it on top of the screen
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNEMENT, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align = ALIGNEMENT, font = FONT)