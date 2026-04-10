# Python Program to Display Personal Biodata

name = "Utkarsha Ghanvat"
age = 20
gender = "Female"
college = "Government College of Engineering Karad"
course = "B.Tech Information Technology"
year = "Second Year"
print("----- PERSONAL BIODATA -----")
print("Name:", name)
print("Age:", age)
print("Gender:", gender)
print("College:", college)
print("Course:", course)
print("Year:", year)

# Program to perform arithmetic operations on two numbers
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("\n--- Arithmetic Operations ---")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
"""
# Swap two numbers using a temporary variable

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

temp = num1
num1 = num2
num2 = temp

print("\nAfter swapping:")
print("First number =", num1)
print("Second number =", num2)

# Swap two numbers without using a temporary variable

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1, num2 = num2, num1

print("\nAfter swapping:")
print("First number =", num1)
print("Second number =", num2)

# Program to calculate Simple Interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100

print("\nSimple Interest =", simple_interest)

# Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)

# Area and Perimeter of Rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area =", area)
print("Perimeter =", perimeter)

# Check positive, negative or zero

num = float(input("Enter a number: "))

if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

# Convert days to years, weeks, and days

days = int(input("Enter number of days: "))

years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
days_left = remaining_days % 7

print("Years =", years)
print("Weeks =", weeks)
print("Days =", days_left)

# Square and cube of a number

num = float(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)

# Demonstrate relational and logical operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a > b :", a > b)
print("a < b :", a < b)
print("a == b :", a == b)
print("a != b :", a != b)

# Logical operators
print("a > 0 and b > 0 :", a > 0 and b > 0)
print("a > 0 or b > 0 :", a > 0 or b > 0)
print("not(a > b) :", not(a > b))

# 1. Program to create a tuple and display its elements
t = (10, 20, 30, 40, 50)
print("Tuple elements:", t)


# 2. Program to find sum and average of tuple elements
t = (10, 20, 30, 40, 50)

total = sum(t)
average = total / len(t)

print("Sum =", total)
print("Average =", average)


# 3. Program to find maximum and minimum in a tuple
t = (15, 8, 25, 3, 10)

print("Maximum =", max(t))
print("Minimum =", min(t))


# 4. Program to demonstrate tuple packing and unpacking
# Packing
t = (10, 20, 30)

# Unpacking
a, b, c = t

print("Tuple:", t)
print("Unpacked values:", a, b, c)


# 5. Program to convert tuple into list
t = (10, 20, 30, 40)

list1 = list(t)

print("Tuple:", t)
print("Converted List:", list1)


# 6. Program to create and perform set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set1:", set1)
print("Set2:", set2)


# 7. Program to find union, intersection and difference of sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))


# 8. Program to remove duplicate elements using set
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print("List without duplicates:", unique_numbers)


# 9. Program to check membership of an element in tuple
t = (10, 20, 30, 40)

num = int(input("Enter element to check: "))

if num in t:
    print("Element is present in tuple")
else:
    print("Element is not present in tuple")


# 10. Program to count occurrences of an element in tuple
t = (10, 20, 30, 20, 40, 20)

num = int(input("Enter element to count: "))

count = t.count(num)

print("Element occurs", count, "times")