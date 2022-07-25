class Person:
    # define instance variable
    def __init__(self, name) -> None:
        self.name = name

    def getName(self):
        return self.name

    def isWorking(self):
        return False

class Employee(Person):
    def isWorking(self):
        return True

human1 = Person('Jack')
print(human1.getName(), human1.isWorking())

human2 = Employee('Michael')
print(human2.getName(), human2.isWorking())

# use issubclass() to check whether a class is the subclass of another class or not
class Base:
    pass

class Derived(Base):
    pass

def issubclassof(class1, class2):
    if issubclass(class1, class2):
        return(f'{class1} is the subclass of {class2}')
    else:
        return(f'{class1} is not the subclass of {class2}')
print(issubclassof(Derived, Base))
print(issubclassof(Derived, Base))

# use isinstance() to determine whether an object is the instance of the class or not
def isinstanceof(object, class1):
    if isinstance(object, class1):
        return (f'{object} is the instance of {class1} class.')

    else:
        return (f'{object} is not the instance of {class1}.')

obj1 = Base()

obj2 = Derived()

print(isinstanceof(obj1, Base))
print(isinstanceof(obj1, Derived))
print(isinstanceof(obj2, Base))
print(isinstanceof(obj2, Derived))



