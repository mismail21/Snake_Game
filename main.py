from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
import time
from food import Food


screen = Screen()

screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

gameison = True
while gameison:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#     Detect collison with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameison = False
        scoreboard.game_over()

# detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameison = False
            scoreboard.game_over()





















screen.exitonclick()