#ASSIGNMENT 1 -  Reverse a given string. 
string = input("Enter a string: ")

reverse = string[::-1]

print("Reversed string:", reverse)


#ASSIGNMENT 2 - Check whether a string is palindrome.
string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
 
 
#ASSIGNMENT 3 - Count vowels and consonants in a string.
string = input("Enter a string: ")

vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for char in string:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)

#ASSIGNMENT 4 - Find the longest word in a sentence. 

sentence = input("Enter a sentence: ")

words = sentence.split()
longest = max(words, key=len)

print("Longest word:", longest)


#ASSIGNMENT 5 - Remove duplicate characters from a string.

string = input("Enter a string: ")

result = ""

for char in string:
    if char not in result:
        result += char

print("String after removing duplicates:", result) 

#ASSIGNMENT 6 Check whether two strings are anagrams.





