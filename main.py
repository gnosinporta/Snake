from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time


# screen creation
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
# the next instruction turns the animation on/and off 
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
    if snake.head.distance(food) < 10:
        print("om nom nom")
        scoreboard.increase_score()
        food.refresh()

    # TODO: detect collision with edges of the screen
    # TODO: of course the snake must grow everytime it eats food
    # TODO: detect collision with itself
    # TODO: show game over in screen


screen.exitonclick()
