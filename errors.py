"""
1. syntax errors:
S + V + O


variable can cause syntax errors
loops can also create syntax errors

2. type errors: this is a kind of error that occurs when using
data type wrongly.

"
1. string -> ''
2. int -> 1
3. boolean -> T or F
4. float -> 1.6
5. list -> [1, 3, 5]
6. tuple -> (1, 3, 5)
7. Dictionary -> {'name': 'Caleb', 'surname': 'Jason'}

"
3. name error:
"""

# name = 'name'
# age = 26
age = 26
print(age)



print('Hello' + ' 5')

# for i in range(10):
#     print(i)


# print(names)


    # Write your logic here

# My name is Caleb

# 2_name = 'Caleb'

# for i in range(100):
#    pass

# with integers, + -> adds 2 or many numbers
# print(5 + 6)

# with strings(text), + -> concatinate 2 or many words
# print('My name is' + ' Caleb')

# print(5*'Hello ')


# age = input(' How old are you? ')

# print(int(age) - 10)



# def subst_from_age():
#     age = float(input('How old are you?: '))


#     if age > 26:
#         print(age - age)
#     else:
#         print(age-10)

# subst_from_age()


def sum(l1, l2, target):

    length = len(l1) if len(l1)>= len(l2) else len(l2)



    for i in range(length):
        if l1[i]+l2[i] == target:
            ans = [l1[i], l2[i]]
            return ans
    return []
 
l = [2, 4, 6, 3, 7, 1]
l1 = [3, 5, 3, 7,6, 9]
k = 10

print(sum(l, l1, k))



def remove_duplicates(list_of_dict):

    seen_element = set()
    new_list = []
    for d in list_of_dict:
        t = tuple(d.items())
        if t not in seen_element:
            seen_element.add(t)
            new_list.append(d)

    return new_list

l = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
print(remove_duplicates(list_of_dict=l))