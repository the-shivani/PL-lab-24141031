# 1. Program to check whether a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 2. Program to find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


# 3. Program to check whether a year is leap year
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 4. Program to check whether a number is prime
num = int(input("Enter a number: "))
prime = True

if num <= 1:
    prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

if prime:
    print("Prime number")
else:
    print("Not a prime number")


# 5. Program to print first n natural numbers using loop
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i, end=" ")


# 6. Program to print multiplication table of a number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 7. Program to calculate factorial of a number using loop
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)



# 8. Program to display Fibonacci series
n = int(input("Enter number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# 9. Program to count digits in a number
num = int(input("Enter a number: "))
count = 0

while num != 0:
    num = num // 10
    count += 1

print("Number of digits =", count)


# 10. Program to reverse a number
num = int(input("Enter a number: "))
reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number =", reverse)
