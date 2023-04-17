# """
# Car:
# properties:
#   color -> green
#   model -> bmw
#   make -> 2023
# methods(behaviour)
#   start()
#   stop()
#   move()

# """


# class User:
    
#     # name
#     # username
#     # bio
#     # pwd
#     # year
#     # billing account

#     #constructor
#     def __init__(self, name, username, pwd, bio):
#         """
#         constructor or dunder init
#         """
#         self.name = name
#         self.username = username
#         self.pwd = pwd
#         self.bio = bio

#     def __str__(self) -> str:
#         return f'{self.username} bio: {self.bio}'
    
#     # methods -> a function inside
#     def like(self):
#         print('👍')
    
#     def deslike(self):
#         print('👎')
    
#     def comment(self, c):
#         print(f'👨🏽‍💻 commented "{c}"')
    
#     def upload(self):
#         print('⏏️')

# caleb = User('Caleb', 'cj', '123456', 'I love cooking')
# print(caleb)
# caleb.comment('This video was lit🔥')
# caleb.like()

# arthur = User('Arthur', 'atr123', 'ilovemango', 'car collector')
# print(arthur)
# arthur.like()


# class Customer:
    
#     def __init__(self, name, username, pwd, adress):
#         """
#         constructor or dunder init
#         """
#         self.name = name
#         self.username = username
#         self.pwd = pwd
#         self.adress = adress

#     def __str__(self) -> str:
#         return f'{self.username} bio: {self.bio}'



""" Inheritance"""


class Employee:
    raise_rate = 1.5

    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.email = ''
        self.salary = salary

    def get_detail(self):

        d = f'First Name: {self.f_name} \nLast Name: {self.l_name} \nEmail: {self.f_name}.{self.l_name}@cupcake&co.com'
        return d
    
    def raise_sal(self):

        return self.salary * self.raise_rate
    


class Developer(Employee):

    raise_rate = 3.5

class Manager(Employee):
    raise_rate = 5
    def __init__(self, f_name, l_name, salary):
        super().__init__(f_name, l_name, salary)
        self.team_members = []

    def add_member(self, member):
        for emp in member:

            self.team_members.append(emp)
            print(f'{member} Has been added to your team')




dev1 = Developer('Caleb', 'Kanku', 2000)
dev2 = Developer('Anvar', 'Maulin', 2500)

emp = Employee("John", "Doe", 500)

manager = Manager('James', "Gordon", 5000)


print(dev1.raise_sal())

print(dev1.get_detail())

print('====================')

print(emp.get_detail())
print(emp.raise_sal())


print('====================')

print(manager.get_detail())
print(manager.raise_sal())
manager.add_member([dev1, dev2])



