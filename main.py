import time
from turtle import Screen

from scoreboard import ScoreBoard
from snake import Snake
from food import Food


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True
count = 1
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend_snake()

    # Detect Wall Collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        is_game_on = False
        score.game_over()

    # Detect Tail collision
    for seg in snake.segments[1:] :
        if snake.head.distance(seg) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
