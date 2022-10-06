from turtle import Turtle
import random

# CONSTANTS
FOOD_LEN = 0.5
FOOD_WID = 0.5
FOOD_SHAPE = "circle"
FOOD_COLOR = "red"
FOOD_SPEED = "fastest"
MARGIN = 280


# TODO: the food must be created in a place where the snake is not present
# TODO: the food must be created in a grid of 20x20 squares
# Sometimes the food gets created in some specific pixels
# where the snake can not touch it. i made a little QA with the 
# basic game so far. the 20x20 grid should sort out the problem 
# aforementioned. (2/9/22)

class Food(Turtle):

    def __init__(self):
        super().__init__()

        # creation of the ball of food
        self.shape(FOOD_SHAPE)
        self.color(FOOD_COLOR)
        self.speed(FOOD_SPEED)
        self.shapesize(stretch_len=FOOD_LEN, stretch_wid=FOOD_WID)
        self.penup()
        self.refresh()

    def refresh(self):
        # creation of the random coordinates of the food
        x_random = random.randint(-MARGIN, MARGIN)
        y_random = random.randint(-MARGIN, MARGIN)
        self.goto(x_random, y_random)
