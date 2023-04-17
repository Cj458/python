# Collection data types
names = ['Caleb', 'Almaz', 'Elena', 'Anvar', 'Arthur']

num = 100
name = 'Caleb'

# to create a list in python, we use square bracket -> []

my_list = [num, name]

salaries = ['Caleb', 2500, 2000, 2000, 2300, 3000, 2500.99]

to_do = ['Take a shower', 'have breakfast', 'have classes', 'Lunch', 'go to university', 'Go to the gym', 'Cook dinner', 'shower and brush teeth']

#            0,                1,               2,            3,            4,                  5,            6,                 7

print(names)

# Accessing an item of a list -> list[index]

# positive index accesses the items of a list from left to right
# negative index accesses the items of a list from right to left
print(to_do[-1])

# changing values of list items  -> list[index] = ' '


to_do[2] = 'Read a book'

print(to_do)


# list methods

# adding an item to the 'end' of the list -> append()

to_do.append('Go to bed')
print(to_do)


# adding an item to the list on a given index(position) -> insert()

to_do.insert(0, 'Wake up')

print(to_do)







