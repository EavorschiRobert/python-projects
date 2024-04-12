import turtle as t


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            square = t.Turtle('square', 20)
            square.color('white')
            square.penup()
            if i > 0:
                square.goto(x=-i * 20, y=0)
            self.snake.append(square)

    def move(self):
        for s in range(len(self.snake) - 1, -1, -1):
            if s == 0:
                self.snake[s].fd(20)
            else:
                position = self.snake[s - 1].position()
                self.snake[s].goto(position[0], position[1])

    def turn_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def turn_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def turn_up(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(90)

    def turn_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)
