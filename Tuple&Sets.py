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