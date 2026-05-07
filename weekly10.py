#ASSIGNMENT 1 :- Demonstrate single inheritance.  

class Parent:
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")


c1 = Child()

c1.show_parent()
c1.show_child()
#ASSIGNMENT 2 :- Program for multilevel inheritance.

class GrandParent:
    def grandparent_method(self):
        print("This is GrandParent class")

class Parent(GrandParent):
    def parent_method(self):
        print("This is Parent class")

class Child(Parent):
    def child_method(self):
        print("This is Child class")


c1 = Child()

c1.grandparent_method()
c1.parent_method()
c1.child_method()
#ASSIGNMENT 3 :- Example of method overriding. 

class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d1 = Dog()

d1.sound()
#ASSIGNMENT 4 :-  Program demonstrating polymorphism.

class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly")


def flying_test(obj):
    obj.fly()

b1 = Bird()
a1 = Airplane()

flying_test(b1)
flying_test(a1) 
#HASSIGNMENT 5 :- Implement encapsulation using getters and setters. 

class Student:

    def __init__(self):
        self.__marks = 0   

    def set_marks(self, marks):
        self.__marks = marks

    
    def get_marks(self):
        return self.__marks


s1 = Student()

s1.set_marks(85)

print("Student Marks =", s1.get_marks())
#ASSIGNMENT 6 :- Real-world OOP case study (Library system).