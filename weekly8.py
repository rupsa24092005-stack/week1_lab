#ASSIGNMENT 1 :- Create a file and write text into it. 
 

file = open("sample.txt", "w")
file.write("Hello, this is a sample file.\n")
file.write("Python file handling example.")
file.close()

print("Data written successfully.")

#ASSIGNMENT 2 :- Read contents of a file.

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

#ASSIGNMENT 3:- Count number of lines in a file.

file = open("sample.txt", "r")

lines = file.readlines()
count = len(lines)

print("Number of lines:", count)

file.close()
#ASSIGNMENT 4 :- File-based student record management system. 

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        file = open("students.txt", "a")
        file.write(roll + "," + name + "," + marks + "\n")
        file.close()

        print("Student record added successfully.")

    elif choice == "2":
        file = open("students.txt", "r")

        print("\nStudent Records:")
        for line in file:
            roll, name, marks = line.strip().split(",")
            print("Roll:", roll, "| Name:", name, "| Marks:", marks)

        file.close()

    elif choice == "3":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")

#ASSIGNMENT 5 :- Copy contents from one file to another. 

source = open("sample.txt", "r")
data = source.read()

destination = open("copy.txt", "w")
destination.write(data)

source.close()
destination.close()

print("File copied successfully.")

#ASSIGNMENT 6 :- Find word frequency from a text file


file = open("sample.txt", "r")

text = file.read().lower()
words = text.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequencies:\n")

for word, count in frequency.items():
    print(word, ":", count)

file.close()