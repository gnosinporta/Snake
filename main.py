from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

MARGIN = 285

# screen creation
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
# the next instruction turns the animation on/off 
# and sets delays for update drawings.
# screen.update() must be called to see the effect
screen.tracer(0)    

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# game loop

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 15:
        # print("om nom nom")
        scoreboard.increase_score()
        food.refresh()
        snake.grow()

    # detectiung collision with walls
    if snake.head.xcor() > MARGIN or snake.head.xcor() < -MARGIN or snake.head.ycor() > MARGIN or snake.head.ycor() < -MARGIN:
        game_is_on = False
        scoreboard.game_over() 

    # detecting collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over() 

screen.exitonclick()
