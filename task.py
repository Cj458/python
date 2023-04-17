class Student:
    def __init__(self, name, age, grade_level):
        self.name = name
        self.age = age
        self.grade_level = grade_level




class School:
    def __init__(self):
        self.students = []



    def add_student(self, name, age, grade_level):
        student = Student(name, age, grade_level)
        self.students.append(student)
        print("Student record added successfully!")

    def get_student(self, name):
        for student in self.students:
            if student.name == name:
                print("Student record found:")
                print("Name:", student.name)
                print("Age:", student.age)
                print("Grade Level:", student.grade_level)
                return
        print("Student record not found.")


school = School()
print('Welcome to AIS record system')
command = ''
while command !='exit':
    command = input('please enter a command for the action you want to do(add, get, exit): ')
    if command == 'add':
        name = input('Name: ')
        age = int(input('age: '))
        grade_level = input('grade_level: ')
        school.add_student(name, age, grade_level)
    elif command == 'get':
        name = input("Enter student name: ")
        school.get_student(name)



        class Animal:
            pass

        class Shelter:
            def __initi__(self,):
                pass

            def add_animal(self, ):
                pass

            def feed_animal(self, animal):
                if animal in self.animals:
                     animal.hunger_level-=1
                     animal.happiness_lvl+=1
                     print()
                else:
                    print('')

            

