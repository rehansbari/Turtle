from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

def set_color():
    R = random.random()
    B = random.random()
    G = random.random()
    timmy.color(R, G, B)
    # This is an example of a tuple which is a data type within Python. Data within a Tuple Cannot be changed. 

def random_walk1():
    timmy.forward(20)
    timmy.right(90)

def random_walk2():
    timmy.back(20)
    timmy.left(90)

choices = [1, 2]
i = 0

timmy.pensize(15)
while i < 100:
    random_choice = random.choice(choices)
    set_color()
    if random_choice == 1:
        random_walk1()
    else:
        random_walk2()
    i += 1
screen = Screen()
screen.exitonclick()