import keyword


"""
strings in programming are a chain of characters.
we use single quote, double or triple quotes for strings.
"""
hello = 'hello world'
hi = " i am Caleb"
a = " here i can use apostrophe ' "

string="""
triple quote is usually used to spread
 a string that spend 
 multiple lines. 
"""


"""
using square bracket and index, we can access a specific character of a string.
negative index return character from behind.
"""

print(hello[0])
print(hello[-1])

'slicing syntax can be used on string too'
# print(hello[0:3 ])

"""
if nothing is supply as starting point, python will assume 0, and if 
nothing is supply as ending point, python will assume the string's length.
"""
print(hello[:3 ])
print(hello[1: ])
print(hello[0:-2 ])


# Index
name = 'Caleb is our teacher'
 #      0123456789101112

last_name = 'Jason'

" sister's cat "

# print(f'{name[0]}. {last_name[1+3]}.' )

text = """bzjbfskbsklbs`kbdkdba
bsfbskmbsmbslmkbklb
avkdsvjkvdjkvdjkvdakjdva
"""

print(name[0:5])


"""
write a program that takes input from the user (first_name, and last name)

you should print out only the initials
"""

my_string = """ 2022 """ # string
# my_string = 2022  # integer
# my_string = " 2022 " # string
# my_string = ' 2022' # string
# my_string = 20.22 # float

print("my_string ") # string
print(my_string) # variable

# print(dir(my_string))