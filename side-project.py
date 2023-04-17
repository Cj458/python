import math 
import turtle as t
import random

win_width = 500
win_height = 500

turtles = 8

t.screensize(win_width, win_height)

class Racer(object):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.turt = t.Turtle()
        self.turt.shape('turtle')
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)

    def move(self):
        r = random.randrange(1, 20)
        self.pos = (self.pos[0], self.pos[1] + r)
        self.turt.pendown()
        self.turt.forward(r)

    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)


def setup_file(name, colors):
    file = open(name, 'w')
    for color in colors:
        file.write(color + '0\n')
    file.close()


def start_game():
    t_list = []
    t.clearscreen()
    t.hideturtle()
    colors = ["red", "green", "blue", "yellow", "pink", "orange", "purple", "black"]
    start = -(win_width/2) + 20

    for t in range(turtles):
        new_posx = start + t*(win_width)//t



