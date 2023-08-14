from turtle import Screen,Turtle
from food import Food
from snake import Snake
import time



screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("green")
screen.title("snake game")
screen.tracer(0)
positions = [(0,0), (-20,0), (-40,0)]
each_part = []

snake = Snake()
food = Food()
food2 = Food()

check = True

#screen.listen()
#screen.onkey(snake.move_up, "w")
#screen.onkey(snake.move_down, "s")
#screen.onkey(snake.move_right, "a")
#screen.onkey(snake.move_left, "d")

while check:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    screen.onkey(snake.move_right, "d")
    screen.onkey(snake.move_left, "a")
    snake.move()
        # if segment.xcor()>600:
        #     segment.setx(-300)
    if snake.each_part[0].distance(food)<15:
        food.create()
        snake.grow()
    if snake.each_part[0].distance(food2) < 15:
        food2.create()
        snake.grow()
    if snake.each_part[0].xcor()>290:
        snake.each_part[0].setx(-290)
    if snake.each_part[0].xcor()<-290:
        snake.each_part[0].setx(290)



    if snake.each_part[0].ycor()>290:
        snake.each_part[0].sety(-290)
    if snake.each_part[0].ycor()<-290:
        snake.each_part[0].sety(290)


    for part in snake.each_part[1:]:
        if snake.each_part[0].distance(part)<10:
            check = False
            print("game over")





screen.exitonclick()