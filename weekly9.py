#ASSIGNMENT 1 :- Create a class and object in Python. 

class Student:
    def display(self):
        print("Hello, I am a student.")

s1 = Student()

s1.display()
#ASSIGNMENT 2 :- Use constructor to initialize object data. 

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Rahul", 20)

s1.show()
#ASSIGNMENT 3 :- Create a class with multiple methods. 

class Calculator:

    def add(self, a, b):
        print("Addition =", a + b)

    def subtract(self, a, b):
        print("Subtraction =", a - b)

    def multiply(self, a, b):
        print("Multiplication =", a * b)

c1 = Calculator()

c1.add(10, 5)
c1.subtract(10, 5)
c1.multiply(10, 5)
#ASSIGNMENT 4 :- Employee management system using class. 

class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("\nEmployee Details")
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

e1 = Employee(101, "Riya", 35000)
e2 = Employee(102, "Aman", 42000)

e1.display()
e2.display()
#ASSIGNMENT 5 :- Bank account simulation using OOP. 


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Insufficient Balance!")

    def show_balance(self):
        print("Current Balance =", self.balance)

b1 = BankAccount("Rahul", 5000)

b1.show_balance()
b1.deposit(2000)
b1.withdraw(3000)
b1.show_balance()
#ASSIGNMENT 6 :- Demonstrate interaction between two objects
