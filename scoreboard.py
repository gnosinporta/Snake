from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0

        # creates the scoreboard and place it on top of the screen
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
        self.hideturtle()

