import time
from turtle import Screen
from ball import Ball
from player import Player
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

player1 = Player(-370)
player2 = Player(370)
ball = Ball()
screen.update()
score = Score()
screen.listen()
screen.onkey(player1.go_up, 'w')
screen.onkey(player1.go_down, 's')
screen.onkey(player2.go_up, 'Up')
screen.onkey(player2.go_down, 'Down')
game_on = True
while game_on:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.xcor() > 370 or ball.xcor() < -370:
        if player1.distance(ball) < 20 or player2.distance(ball) < 20:
            ball.hit()
        elif ball.xcor() > 370:
            ball.point()
            score.add_point(1)
        else:
            ball.point()
            score.add_point(2)

    screen.update()
    ball.move()

screen.exitonclick()
