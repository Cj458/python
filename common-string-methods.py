my_string = 'Caleb is our python teacher'


print(dir(my_string))

# upper case

print(my_string.upper())

# lower

print(my_string.lower())

# replace a character or an entire string

print(my_string.replace('Caleb', 'Jason'))

# split your string in elements of a list
print(my_string.split(' '))

# join method joins substring into a whole strinng
a = my_string.split(' ')

j = '-'.join(a)

print(j)
