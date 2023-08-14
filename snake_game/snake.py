from turtle import Turtle

POSITIONS = [(0,0), (-20,0), (-40,0)]

class Snake():
    def __init__(self):
        self.each_part = []
        self.create_snake()
    def creatingpart(self,position):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.setposition(x=position[0], y=position[1])
        self.each_part.append(turtle)


    def create_snake(self):
        for position in POSITIONS:
           self.creatingpart(position)
    def move(self):

        for segment_number in range(len(self.each_part) - 1, 0, -1):
            nx = self.each_part[segment_number - 1].xcor()
            ny = self.each_part[segment_number - 1].ycor()
            self.each_part[segment_number].goto(nx, ny)

        self.each_part[0].forward(20)

    def move_right(self):
        self.each_part[0].right(90)

    def move_left(self):
        self.each_part[0].left(90)


    def grow(self):
        self.creatingpart(self.each_part[-1].position())
