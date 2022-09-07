from turtle import Turtle

# this list of tuples stores the starting position of the snake in the beginning of the game
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]

# this constant stores the moving distance of each step of the snake
MOVE_DISTANCE = 20

# constants of direction
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # TODO: of course the snake must grow everytime it eats food

    def __init__(self):
        # This first list contains Turtles that form the body
        self.segments = []  
        self.create_snake()
        self.head = self.segments[0]

    # snake body creation
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # adds a new segment to the snake
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    # snake moves
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    # this function adds another segment to the snake everytime it eats
    def grow(self):
        self.add_segment(self.segments[-1].position())

    # all these following methods define how the snake turns
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            