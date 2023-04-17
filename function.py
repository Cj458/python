import random
"""
a function is a piece of code that does a specific thing.

to create of define a function, we use the key word:

terms: 
1. define -> def
2. call -> using the func
3. parameter -> a piece of info that you give to to your function to use
4. return -> the data your function output: return

def function_name():
    your code
"""

#naming your function

#snake case -> 

print(2*2)


print(max(2, 5, 8, 20))
print(min(2, 5, 8, 20))

# creating our own func

def hi() :
    print('Hi')

# calling a function
hi()

# func with parameters
def add(x, y):
    return x+y
    
s= add(5, 5)

print(s)


# You need to put this block as a function

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


