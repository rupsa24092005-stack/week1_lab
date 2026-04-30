#ASSIGNMENT 1 -  Create a dictionary with at least 5 key-value pairs.

dic = {
    "name": "Riya",
    "age": 20,
    "course": "Computer Science",
    "city": "Kolkata",
    "marks": 85
}

print("Dictionary:", dic)

# ASSIGNMENT 2- Search for a key in a dictionary.


key = input("Enter the key to search: ")

if key in dic:
    print("Key found!")
    print("Value:", dic[key])
else:
    print("Key not found in the dictionary.")


# ASSIGNMENT 3 -  Count frequency of each character in a string using dictionary.

string = input("Enter a string: ")
freq = {}

for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character Frequency:")
for key, value in freq.items():
    print(key, ":", value)

# ASSIGNMENT 4 - Student marks management system using dictionary

students = {}

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully!\n")

def display_students():
    if not students:
        print("No records found!\n")
    else:
        print("Student Records:")
        for name, marks in students.items():
            print(name, ":", marks)
        print()

def search_student():
    name = input("Enter student name to search: ")
    if name in students:
        print(name, "marks =", students[name], "\n")
    else:
        print("Student not found!\n")

def update_marks():
    name = input("Enter student name to update: ")
    if name in students:
        marks = int(input("Enter new marks: "))
        students[name] = marks
        print("Marks updated successfully!\n")
    else:
        print("Student not found!\n")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print("Student deleted successfully!\n")
    else:
        print("Student not found!\n")


while True:
    print("===== Student Marks Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_marks()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")


# ASSIGNMENT 5 - Sort dictionary by values.
# ASSIGNMENT 6 -  Merge two dictionaries without using built-in methods.


'''
   SORT DICTONARY BY VALUES 

   sorted_dict = dict(sorted(student.items(), key=lambda item: item[1]))

   MERGE TWO DICT WITHOUT BUILT IN METHODS 

   merged = {}

   for key in d1:
    merged[key] = d1[key]

   for key in d2:
    merged[key] = d2[key]

print(merged)


'''
