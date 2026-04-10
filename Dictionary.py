# 1. Program to create a dictionary of student details
student = {
    "Name": "Utkarsha",
    "Age": 20,
    "Course": "B.Tech IT",
    "College": "Government College of Engineering Karad"
}

print("Student Details:", student)


# 2. Program to access keys, values and items of a dictionary
student = {"Name": "Rahul", "Age": 19, "Course": "B.Tech"}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# 3. Program to add and update dictionary elements
student = {"Name": "Amit", "Age": 20}

# Adding new element
student["Course"] = "B.Tech"

# Updating element
student["Age"] = 21

print("Updated Dictionary:", student)


# 4. Program to delete elements from dictionary
student = {"Name": "Amit", "Age": 20, "Course": "B.Tech"}

del student["Age"]

print("Dictionary after deletion:", student)


# 5. Program to count frequency of words in a sentence using dictionary
sentence = input("Enter a sentence: ")
words = sentence.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequency:", freq)


# 6. Program to merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}

print("Merged Dictionary:", merged)


# 7. Program to convert hexadecimal to binary using dictionary
hex_to_bin = {
    "0": "0000", "1": "0001", "2": "0010", "3": "0011",
    "4": "0100", "5": "0101", "6": "0110", "7": "0111",
    "8": "1000", "9": "1001", "A": "1010", "B": "1011",
    "C": "1100", "D": "1101", "E": "1110", "F": "1111"
}

hex_num = input("Enter hexadecimal number: ").upper()

binary = ""
for digit in hex_num:
    binary += hex_to_bin[digit]

print("Binary equivalent:", binary)


# 8. Program to find student with highest marks
students = {
    "Amit": 85,
    "Rahul": 92,
    "Sneha": 88
}

top_student = max(students, key=students.get)

print("Student with highest marks:", top_student)
print("Marks:", students[top_student])


# 9. Program to sort dictionary by keys and values
data = {"b": 2, "a": 5, "c": 1}

print("Sorted by keys:", dict(sorted(data.items())))
print("Sorted by values:", dict(sorted(data.items(), key=lambda x: x[1])))


# 10. Program to demonstrate dictionary comprehension
squares = {x: x*x for x in range(1, 6)}

print("Dictionary using comprehension:", squares)