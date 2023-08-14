from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
        self.create()


    def create(self):
        randomy = random.randint(-275, 275)
        randomx = random.randint(-275, 275)
        self.goto(randomx, randomy)
