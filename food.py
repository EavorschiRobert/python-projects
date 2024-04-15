import turtle as t
import random


class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_position = (random.randint(-260, 260), random.randint(-260, 260))
        self.goto(random_position)
