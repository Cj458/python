# print("hello world7&****35353")

# " "
# ' '
# # data types.

# """
# text -> string
# number -> 10, 0, 1 -12, 329494959595 -> integer int
#         float, 2.5, 92.99

# boolean -> True or False
# """

# bool, hello = True, False

# number = 10
# string = 'hello'


# decimal_ = 2.5


# print(number * string)





# print(10)
# print("10")
# print(4*4)

# print(10//2)



import turtle

pen = turtle.Turtle()

pen.speed(10)

screen = turtle.Screen()

screen.bgcolor('yellow')

turtle.fillcolor('white')
turtle.begin_fill()

for i in range(36):
        pen.forward(18)
        pen.right(10)
        
turtle.end_fill() 


for i in range(36):
        pen.forward(12)
        pen.left(10)

pen.penup()
pen.goto(0,138)
pen.pendown()

for i in range(36):
        pen.forward(8)
        pen.left(10)

turtle.end_fill()

turtle.exitonclick()


import turtle

pen = turtle.Turtle()
pen.speed(10)
screen = turtle.Screen()
screen.bgcolor("Yellow")

for x in range(36):
  pen.forward(16)
  pen.right(10)

for x in range(36):
  pen.forward(12)
  pen.left(10)

pen.penup()
pen.goto(0,138)
pen.pendown()

for x in range(36):
  pen.forward(8)
  pen.left(10)

pen.penup()
pen.goto(-15,185)
pen.pendown()
pen.circle(6)

pen.penup()
pen.goto(15,185)
pen.pendown()
pen.circle(6)

pen.penup()
pen.goto(-15,160)
pen.pendown()
pen.right(80)
pen.circle(15,180)



