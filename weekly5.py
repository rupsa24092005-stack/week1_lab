# ASSIGNMENT 1 -  Create a list and display its elements.


my_list = [10, 20, 30, 40, 50]

print("Elements of the list are:")
for item in my_list:
    print(item) 

#ASSIGNMENT 2 -  Find maximum and minimum element in a list.

numbers = [10,25,50,60,75,42,50,90]
maximum = max(numbers)
minimum = min(numbers)

print("List:", numbers)
print("Maximum element:", maximum)
print("Minimum element:", minimum)


#ASSIGNMENT 3 -  Count even and odd numbers in a list.

numbers = [10, 15, 22, 33, 40, 55]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("List:", numbers)
print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)

# ASSIGNMNET 4 -  Remove duplicate elements from a list.

numbers = [10, 20, 30, 20, 40, 10, 50 ,60]

unique_numbers = list(set(numbers))

print("Original List:", numbers)
print("List after removing duplicates:", unique_numbers)

# ASSIGNMENT 5 -  Find second largest element in a list.

n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

numbers.sort()

second_largest = numbers[-2]

print("List:", numbers)
print("Second largest element:", second_largest)

'''
    ROTATE A LIST BY K POSITION 

    IT'S BASICALLY MEAN MOVE THE ELEMENTS FROM K TO EITHER LEFT OR RIGHT, IN THE 
    BELOW EXAMPLE THE LAST 3 ELEMENTS MOVED TO FIRST BECAUSE K = 2 (FROM INDEX 2) AND IT IS TO THE LEFT


    lst = [1,2,3,4,5]
    k = 2

    rotated = lst[k:] + lst[:k]
    print(rotated)

    IF K = 2 BUT TO THE RIGHT THEN THE ELEMENTS AFTER INDEX 2 (LAST 2 ELEMENTS) MOVED TO 
    THE FIRST 

    lst = [1,2,3,4,5]
    k = 2

    rotated = lst[-k:] + lst[:-k]
    print(rotated)


    REMARKS :
    ASSIGNMENT CHECKED 
    SCORE 7 / 10



'''