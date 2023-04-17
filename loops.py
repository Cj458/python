

# import turtle as t

# """
# 1. counting loops: this is a type of loop that let us repeat an action
# a certain number of time.

# we use 'for'
# """

# turtle = t.Turtle()
# turtle.speed(10)
# turtle.shape('turtle')

# screen = t.Screen()

# screen.screensize()
# screen.bgcolor('yellow')

# # 1st circle
# for x in range(36):
#     turtle.forward(18)
#     turtle.right(10)

# # 2nd circle
# for x in range(36):
#     turtle.forward(14)
#     turtle.left(10)

# #moving the turtle to draw the 3rd circle
# turtle.penup()
# turtle.goto(0, 160)
# turtle.pendown()

# # 3rd circle
# for x in range(36):
#     turtle.forward(10)
#     turtle.left(10)

# # right eye
# turtle.penup()
# turtle.goto(45, 210)
# turtle.pendown()


# for x in range(36):
#     turtle.forward(2)
#     turtle.left(10)

# # left eye
# turtle.penup()
# turtle.goto(-38, 210)
# turtle.pendown()


# for x in range(36):
#     turtle.forward(2)
#     turtle.left(10)




# # moth
# turtle.penup()
# turtle.goto(-10, 170)
# turtle.pendown()

# for x in range(18):
#     turtle.forward(2)
#     turtle.left(2)

# # nose
# turtle.penup()
# turtle.goto(0, 210)
# turtle.pendown()
# turtle.right(90)
# turtle.forward(10)
# turtle.right(60)
# turtle.forward(8)

# # right arm

# #left arm

# turtle.hideturtle()




# t.exitonclick()


"""
2. cnditional loops: this is a type of loop that runs as long as a condition is True


we use 'while'
"""
import random
# exercise one

number = random.randint(0, 100)
guess = int(input(" I'm thinking of a number from 0 to 100. what is it?: "))


life = 5
# 
# number_if_tries = 0

while guess != number:
    if guess < number:
        print('Your guess is too low...')
    elif guess > number:
        print('Your guess is too high...')
    guess = int(input('Try again... '))
    life -= 1

    if life == 0:
        
        print('Game Over!')
        print(f'The number was {number}')

        res = input('Would you like to play again? Type y or n')
        
        if res == 'y':
            guess = int(input(" I'm thinking of a number from 0 to 100. what is it?: "))
        else:
            break

else:
  print(f" congratulations! {guess} was the correct number. ")
  print(f"GG")


