from turtle import Turtle
import random


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
