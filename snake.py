import turtle as t


class Snake:
    def __init__(self):
        self.snake = []
        self.head = 0
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            x = -i * 20
            self.add_segment((x, 0))
        self.head = self.snake[0]

    def add_segment(self, position):
        square = t.Turtle('square', 20)
        square.color('white')
        square.penup()
        square.goto(x=position[0], y=position[1])
        self.snake.append(square)

    def increase_snake(self):
        self.add_segment(self.snake[-1].position())

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
