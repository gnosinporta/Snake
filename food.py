from turtle import Turtle
import random

# TODO: the food must be created in a place where the snake is not present
# TODO: the food must be created in a grid of 20x20 squares

class Food(Turtle):

    def __init__(self):
        super().__init__()

        # creation of the ball of food
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        # creation of the random coordinates of the food
        x_random = random.randint(-280, 280)
        y_random = random.randint(-280, 280)
        self.goto(x_random, y_random)

        # TODO: the 20x20 grid should sort out the problem aforementioned. Sometimes the food
        # (...continues) gets created in some specific pixels where the snake can not
        # touch it. Made a little QA with the basic game so far (2/9/22)
