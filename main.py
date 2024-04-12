import time
import turtle as t
import snake as s

screen = t.Screen()
screen.bgcolor('black')
screen.title('My Snake Game')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
snake = s.Snake()

screen.onkey(key='Left', fun=snake.turn_left)
screen.onkey(key='Right', fun=snake.turn_right)
screen.onkey(key='Up', fun=snake.turn_up)
screen.onkey(key='Down', fun=snake.turn_down)
still_playing = True
while still_playing:
    snake.move()
    time.sleep(0.1)
    screen.update()


screen.exitonclick()
