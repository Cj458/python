
""" 1. arithmetic operators"""
# + : add
# - : subst
# * : multiply
# / : float division
# // : int
# ** : power/ exponent
# % : remainder

print((5+4)*5**2)

# parentheses
# exponent
# multiplication or division
# addition / substraction

""" 2. logical operators"""

# and: if boy and 18 = army --> True or False
# or : if girl or boy = army --> True

# boy = True

# not boy

""" Exercise"""

# colors = ['red', 'green', 'brown', 'white', 'black']

# users = input('Enter your fav color: ')

# if users in colors:
#     print('yay, we have the same fav color')

# else:
#     print(':)')


# Comparative operators


# is_admin = False
# is_active = True
# is_stuff = True

# if is_admin and is_active:
#     print('ban')


# if is_admin or is_stuff:
#     print('the support team will review your concerns')


#Comparison operators

"""
We use these in situations where we want to compare a variable with a value
these are:
> greater than
>= greater or equal than
< less than
<= less or equal than
== equal than
!= not equal
example:


"""
# temperature = int(input('what is the weather like? '))
# if temperature > 35:
#     print(" it's a hot day today")

# if temperature < 20:
#     print(" it's a chill day today")

# if temperature < 10:
#     print(" it's a cold day today")

"""

if the temp is greater then 35, tell the user that it's hot and they should wear shorts

if the temp less than 20, tell the user that it's chill and they should wear a jacket

if the temp is less than 10, tell them that it's cold.

"""


"""
exercise 1:
"""

# name = input("Enter your name: ")


# if len(name) < 3:
#     print("Name must be at least 3 characters")

# elif len(name) > 50:
#     print("Name can be a maximum of 50 characters")

# else:
#     print('name looks good')

"""
exercise 2:
"""

# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g? ')

# if unit.upper() == 'L':
#     converted = weight * 0.45
#     print(converted)
# else :
#     converted = weight / 0.45
#     print(converted)

"""
4. membership operator
"""

# in, not in: -> True/False

my_list = ['Fifa', 'COD', 'Mortal Kombat', 'Assassin Creed']

if 'Fortnite'  in my_list:
    # do something
    pass
else:
    # add it
    pass


"""
Assignment operators
"""
# =
# +=: increament by a value
# -=: decreament
# *=: multipy
# /=:

my_list2 = []

# print(len(my_list2))

# if len(my_list2) == 0:
#     my_list2.append(1)

#     i = my_list2[0]
#     i+=5
#     my_list2.append(i)


print(my_list2)

salaries = [2000, 2500, 3000]

# for salary in salaries:
#     if salary == 2000:
#         salary+=500
#         print(salary)
#     if salary == 2500:
#         salary-=1500
#         print(salary)
#     else:
#         print(salary)


"""
    Indentity operator:
    is: returns True if both variables are the same
    not is: Returns True if both variables are not the same object
"""

x = 10
y = 10
# print(y is x)


"""
Words filter, 
ask the user to rengister to your system, 
ask the for their email address, user name and password

create a list of bab words 
when the user input a bad word as input, change the bad to Hello world
and print the email, usename and password

"""

# email = input('Enter your email: ').lower()
# user_name = input('User name: ').lower()
# password = input('Create a password: ').lower()

# bad_words_filter = ['fool', 'stupid', 'bastard']

# for word in bad_words_filter:
#     if word in user_name:
#         user_name = 'hello'
# print(f'your credentials are {email} {user_name} {password}')
    







