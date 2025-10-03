# Object-Oriented Programming (OOP) in Python

## Core Concepts
- **Parent class** & **Child class**
- **Inheritance**
- **Method overloading / overriding**
- **Classes and Objects**
- **Methods**
- **Variables**
  - Class variables (shared across all objects)
  - Instance variables (unique to each object)
- **Instance of class** = a created object

---

## Example: `Person` Class
```python
class Person:
    count = 0   # Class variable

    def __init__(self, name, age):
        self.name = name          # Instance variable
        self.age = age
        Person.count += 1         # Update class variable

    def get_name(self):
        print(f"Name is {self.name}")

    def get_age(self):
        print(f"Age is {self.age}")

    def get_info(self):
        print(f"Name is {self.name}, and age is {self.age}")

    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}")

    def return_count(self):
        return Person.count
```

# Usage
```Python
alireza = Person("Alireza", 35)
alireza.get_name()     # Name is Alireza
alireza.get_age()      # Age is 35
alireza.get_info()     # Name is Alireza, and age is 35
alireza.birthday()     # Happy birthday Alireza
alireza.get_age()      # Age is 36

mini = Person("Mina", 3)
mini.get_info()        # Name is Mina, and age is 3

fati = Person("Fatemeh", 1)
fati.get_info()        # Name is Fatemeh, and age is 1

print(f"At the moment I have {alireza.return_count()} persons.")

Output (example):

Name is Alireza
Age is 35
Name is Alireza, and age is 35
Happy birthday Alireza
Age is 36
Name is Mina, and age is 3
Name is Fatemeh, and age is 1
At the moment I have 3 persons.
```
# Key Notes

__init__ is the constructor, called automatically when an object is created.

count is a class variable → shared across all objects.

self.name, self.age are instance variables → unique to each object.

Each object = one instance of the class.