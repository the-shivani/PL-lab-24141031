# 1. Program to find length of a string
text = input("Enter a string: ")
length = len(text)
print("Length of string =", length)


# 2. Program to reverse a string
text = input("Enter a string: ")
reverse = text[::-1]
print("Reversed string =", reverse)


# 3. Program to check whether a string is palindrome
text = input("Enter a string: ")
if text == text[::-1]:
    print("String is Palindrome")
else:
    print("String is Not Palindrome")


# 4. Program to count vowels and consonants in a string
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels =", vowel_count)
print("Consonants =", consonant_count)


# 5. Program to convert string to upper and lower case
text = input("Enter a string: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())


# 6. Program to count frequency of characters in a string
text = input("Enter a string: ")
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character Frequency:")
for key in freq:
    print(key, ":", freq[key])


# 7. Program to remove spaces from a string
text = input("Enter a string: ")
result = text.replace(" ", "")
print("String without spaces:", result)


# 8. Program to replace a word in a string
text = input("Enter a sentence: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

result = text.replace(old_word, new_word)
print("Updated string:", result)


# 9. Program to split and join strings
text = input("Enter a sentence: ")

split_words = text.split()
print("Split string:", split_words)

joined_string = "-".join(split_words)
print("Joined string:", joined_string)


# 10. Program to check whether two strings are anagrams
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")