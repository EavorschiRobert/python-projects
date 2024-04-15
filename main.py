import time
import turtle as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = t.Screen()
screen.bgcolor('black')
screen.title('My Snake Game')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = ScoreBoard()
screen.onkey(key='Left', fun=snake.turn_left)
screen.onkey(key='Right', fun=snake.turn_right)
screen.onkey(key='Up', fun=snake.turn_up)
screen.onkey(key='Down', fun=snake.turn_down)
still_playing = True
while still_playing:
    snake.move()
    time.sleep(0.1)
    screen.update()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase_snake()
        score.add_score()
    #detect wall collision
    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        still_playing = False
        score.game_over()
    #detect tail collision
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            still_playing = False
            score.game_over()

screen.exitonclick()
