# 1. Write a Python program to import built-in 
# array module and display the namespace of the said module. 
class Exercise1:
    import array
    for i in array.__dict__:
        print(i)
# 2. Write a Python program to create a class and display the namespace of the said class.

class py_solution:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
for name in py_solution.__dict__:
    print(name)

# 3. Write a Python program to create an instance 
# of a specified class and display the namespace of the said instance.

class Animal:
    place_birth = 'Malaysia'
    owner = 'Alex'
    def __init__(self, name, age, type, gender) -> None:
        self.name = name
        self.age= age
        self.type = type
        self.gender = gender

    def display(self):
        print(f'This is a {self.type}.It\'s name is {self.name} and is {self.age} years old and is a {self.gender}.')
    
dog = Animal('Max', 5, 'Golden Retriever', 'boy')
dog.display()
print(dog.place_birth, dog.owner)
for i in dog.__dict__:
    print(i)

# # 4. 'builtins' module provides direct access to all 'built-in' identifiers of Python.
# Write a python program which import the abs() function using the builtins module, display the documentation of abs() function and find the absolute value of -155.

class BuiltIn:
    from builtins import abs
    def findAbs(number) -> int:
        return abs(number)
    
    help(abs) #prints the description of the method
    print(findAbs(-155))

# Define a Python function Studentent(). Using function attributes display the names of all arguments.
class Student:
    def Studentent(id, name, school, classroom):
        return f'{name}\'s Studentent id is {id}. He Studenties in {school} and he belongs to {classroom}.'
    
    print(Studentent('D3638', 'Kingston', 'Imperial London College', 'F4T01A'))

# 6. Write a Python function Studentent_data () which will print the id of a Studentent (Studentent_id). If the user passes an argument Studentent_name or 
# Studentent_class the function will print the Studentent name and class
class Kwargs:
    def Studentent_data(id, **kwargs):
        sentence = f'Studentent ID: {id}'
        if 'name' in kwargs:
            return sentence.join(f"\nStudentent Name: ${kwargs['name']}")
        if 'age' in kwargs:
            return sentence.join(f"\nStudentent Age: ${kwargs['age']}")

        return sentence
    print(Studentent_data('D3727', name='JK Rowling', age='16'))

# Write a simple Python class named Studentent and display its type. Also, display the 
# __dict__ attribute keys and the value of the __module__ attribute of the Studentent class
class Student(Student):
    print(type(Student), Student.__dict__.keys(), Student.__module__)
    