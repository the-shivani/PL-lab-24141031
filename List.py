# 1. Program to create and display a list
numbers = [10, 20, 30, 40, 50]
print("List elements:", numbers)


# 2. Program to find sum and average of list elements
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)

print("Sum =", total)
print("Average =", average)


# 3. Program to find maximum and minimum element in a list
numbers = [15, 8, 25, 3, 10]

print("Maximum =", max(numbers))
print("Minimum =", min(numbers))


# 4. Program to sort elements of a list
numbers = [5, 2, 8, 1, 9]

numbers.sort()
print("Sorted list:", numbers)


# 5. Program to remove duplicate elements from a list
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_list = list(set(numbers))
print("List after removing duplicates:", unique_list)


# 6. Program to search an element in a list
numbers = [10, 20, 30, 40, 50]

element = int(input("Enter element to search: "))

if element in numbers:
    print("Element found in list")
else:
    print("Element not found")


# 7. Program to merge two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2
print("Merged list:", merged_list)


# 8. Program to count even and odd numbers in a list
numbers = [10, 15, 20, 25, 30]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)


# 9. Program to find second largest element in a list
numbers = [10, 25, 8, 40, 15]

numbers.sort()
second_largest = numbers[-2]

print("Second largest element:", second_largest)


# 10. Program to demonstrate list slicing
numbers = [10, 20, 30, 40, 50, 60]

print("Original list:", numbers)
print("First three elements:", numbers[:3])
print("Last three elements:", numbers[-3:])
print("Elements from index 2 to 4:", numbers[2:5])