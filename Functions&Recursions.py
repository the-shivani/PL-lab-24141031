# 1. Program to define and call a function
def greet():
    print("Hello, welcome to Python programming!")

greet()


# 2. Program to pass arguments to a function
def add(a, b):
    result = a + b
    print("Sum =", result)

add(10, 5)


# 3. Program to return multiple values from a function
def calculate(a, b):
    sum = a + b
    difference = a - b
    return sum, difference

s, d = calculate(10, 5)
print("Sum =", s)
print("Difference =", d)


# 4. Program to calculate factorial using function
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))


# 5. Program to calculate factorial using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

num = int(input("Enter a number: "))
print("Factorial (recursion) =", factorial_recursive(num))


# 6. Program to generate Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("Enter number of terms: "))
for i in range(terms):
    print(fibonacci(i), end=" ")


# 7. Program to demonstrate lambda function
square = lambda x: x * x

num = int(input("Enter a number: "))
print("Square =", square(num))


# 8. Program to use built-in functions
numbers = [5, 10, 15, 20]

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))


# 9. Program to demonstrate scope of variables
x = 10   # Global variable

def show():
    x = 5  # Local variable
    print("Inside function x =", x)

show()
print("Outside function x =", x)


# 10. Program to check prime number using function
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")