import turtle
import random
"""
1. for loops`;
counting loops because it allows you to repeat a loop an certain number of time 



"""
# while 'Nari feels great':
#     'listen to Lil Nas x'



"""
2. while loop
conditional loop

because it will stop until a condition changes
"""

# n = 1
# for n in range(10000000):
#     n*n
# t = turtle.Turtle()


# t.shape('turtle')
# t.speed(10)

# t.pencolor('black')

# t.fillcolor('yellow')

# t.begin_fill()
# for x in range(36):
#     t.forward(16)
#     t.right(10)


# t.end_fill

# for x in range(36):
#     t.forward(12)
#     t.left(10)

# t.end_fill

# t.penup()
# t.goto(0, 138)
# t.pendown()

# for x in range(36):
#     t.forward(9)
#     t.left(10)


# t.penup()
# t.goto(-17, 185)
# t.pendown()
# for x in range(36):
#     t.forward(1)
#     t.left(10)

# t.penup()
# t.goto(17, 185)
# t.pendown()
# for x in range(36):
#     t.forward(1)
#     t.left(10)

# t.penup()
# t.goto(-17, 160)
# t.pendown()

# t.right(80)
# t.circle(15, 180)

# # for x in range(18):
# #     t.forward(20)
# #     t.left(10)
# t.hideturtle()

# turtle.exitonclick()


"""
2. while loop
conditional loop

because it will stop until a condition changes

break
continue
else
"""
import string


# my_list = ['hello', 'there', 'hi']
random_word = random.choice(my_list)

guess = input("I'm thinking of a number from 1 to 20. what is it? ").lower()

number = random.randint(1, 100)
# 10

# use number as well

guess = int(input("I'm thinking of a number from 1 to 20. what is it? "))

life = 5

while guess != random_word:
    
    guess = input('Try again: ').lower()

print(f" congrants. the number was {random_word}. you won")


while guess != number:
    #   6        10
    if guess < number:
        print('Your number is too low...')
    else:
        print('Your number is too high..')
    guess = int(input('Try again: '))

print(f" congrants. the number was {number}. you won")


# Word guesser
# 
# :




"""
Infinite loop
"""

# i = 0

# while i < 5:
#     print(f'Hello - {i}')
#     i+=1

"""
break
continue
"""


adjectives = ['sleepy', 'slow', 'wet', 'fat', 'red', 'interesting','exhausting', 'fast', 'dry', 'thin', 'tremendous', 'luxurious']
uppers = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lowers = list('abcdefghijklmnoprstuvwxyz')
nouns = ['cat', 'jenitor', 'teacher', 'gamer', 'bear']
characters = list("""!@#$%^&*(_)+=][}{;:.<>?'""")


print('Welcome to password generator!')

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_ch = random.choice(characters)
    upper = random.choice(uppers)
    lower = random.choice(lowers)

    pwd = adjective+noun+ str(number)+ special_ch + upper+ lower

    print(f'Your pwd is {pwd}')

    res = input('Would you like another pwd? Type y or n: ')

    if res == 'n':
        break

