import time
from turtle import Screen
from snake import Snake


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

screen.update()
snake = Snake()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # segments[0].left(90)



screen.exitonclick()
