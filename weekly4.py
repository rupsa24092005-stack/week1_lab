# assignment 1 -  Write a function to add two numbers.

def add_numbers(a, b):
    return a + b

a = int(input("Enter your first number :- "))
b = int(input("Enter your second number :- "))
result = add_numbers(a, b)
print("Sum =", result)


# assignment 2 -  Function to find factorial of a number

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

num = int(input("Enter your number :- "))
print("Factorial of", num, "is", factorial(num))

# assignment 3 -  Function to check prime number

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")


# assignment 4 -  Menu-driven program using functions.

def add_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =", a + b)

def even_odd():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

def check_prime():
    n = int(input("Enter a number: "))
    if n <= 1:
        print("Not a prime number")
        return

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

# Menu-driven program
while True:
    print("\n--- MENU ---")
    print("1. Add two numbers")
    print("2. Check Even or Odd")
    print("3. Check Prime Number")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_numbers()
    elif choice == 2:
        even_odd()
    elif choice == 3:
        check_prime()
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")




# assignment 5 -  Recursive function for Fibonacci series.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter number of terms: "))

print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i), end=" ")
# assignment 6 -  Function to check Armstrong number.

def is_armstrong(n):
    num = n
    digits = len(str(n))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** digits
        num //= 10

    return total == n
num = int(input("Enter a number: "))

if is_armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")

