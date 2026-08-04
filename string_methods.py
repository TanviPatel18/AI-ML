# ==============================
# Python String Methods Examples
# ==============================

# Original string
text = "Hello Python 123"

print("Original String :", text)
print()


# --------------------------------
# isalpha()
# Checks if the string contains ONLY letters.
# No spaces, numbers, or symbols are allowed.
# --------------------------------
print("Python".isalpha())      # True
print("Python123".isalpha())   # False
print("Hello World".isalpha()) # False (contains space)
print()


# --------------------------------
# isalnum()
# Checks if the string contains only letters and numbers.
# Spaces and symbols are NOT allowed.
# --------------------------------
print("Python123".isalnum())   # True
print("Python 123".isalnum())  # False (space)
print("Python@123".isalnum())  # False (@ symbol)
print()


# --------------------------------
# isdecimal()
# Checks if the string contains only decimal digits (0-9).
# --------------------------------
print("12345".isdecimal())     # True
print("12.5".isdecimal())      # False (.)
print("123a".isdecimal())      # False (letter)
print()


# --------------------------------
# lower()
# Converts all letters to lowercase.
# --------------------------------
print("HELLO".lower())         # hello
print()


# --------------------------------
# islower()
# Checks whether all letters are lowercase.
# --------------------------------
print("python".islower())      # True
print("Python".islower())      # False
print()


# --------------------------------
# upper()
# Converts all letters to uppercase.
# --------------------------------
print("python".upper())        # PYTHON
print()


# --------------------------------
# isupper()
# Checks whether all letters are uppercase.
# --------------------------------
print("PYTHON".isupper())      # True
print("Python".isupper())      # False
print()


# --------------------------------
# title()
# Capitalizes the first letter of every word.
# --------------------------------
print("welcome to python".title())   # Welcome To Python
print()


# --------------------------------
# startswith()
# Checks whether a string starts with a given substring.
# --------------------------------
print("Python Programming".startswith("Python"))  # True
print("Python Programming".startswith("Java"))    # False
print()


# --------------------------------
# endswith()
# Checks whether a string ends with a given substring.
# --------------------------------
print("report.pdf".endswith(".pdf"))   # True
print("report.pdf".endswith(".txt"))   # False
print()


# --------------------------------
# split()
# Splits a string into a list.
# Default separator is space.
# --------------------------------
sentence = "I Love Python"

words = sentence.split()

print(words)        # ['I', 'Love', 'Python']
print(type(words))  # <class 'list'>
print()


# Split using a custom separator
data = "apple,mango,banana"

print(data.split(","))   # ['apple', 'mango', 'banana']
print()


# --------------------------------
# strip()
# Removes spaces (or specified characters)
# from the beginning and end of the string.
# --------------------------------
name = "   Python   "

print(name.strip())     # Python

text = "***Hello***"

print(text.strip("*"))  # Hello
print()


# --------------------------------
# lstrip()
# Removes characters from the LEFT side only.
# --------------------------------
text = "   Hello"

print(text.lstrip())    # Hello
print()


# --------------------------------
# rstrip()
# Removes characters from the RIGHT side only.
# --------------------------------
text = "Hello   "

print(text.rstrip())    # Hello
print()


# --------------------------------
# join()
# Joins elements of a list into a single string.
# --------------------------------
languages = ["Python", "Java", "C++"]

print("-".join(languages))     # Python-Java-C++
print(" ".join(languages))     # Python Java C++
print(",".join(languages))     # Python,Java,C++
print()


# --------------------------------
# find()
# Returns the index of the FIRST occurrence.
# Returns -1 if not found.
# --------------------------------
text = "Welcome to Python"

print(text.find("Python"))   # 11
print(text.find("to"))       # 8
print(text.find("Java"))     # -1
print()


# --------------------------------
# rfind()
# Returns the LAST occurrence of a substring.
# --------------------------------
text = "apple mango apple banana"

print(text.find("apple"))     # 0
print(text.rfind("apple"))    # 12
print()


# --------------------------------
# count()
# Counts how many times a substring appears.
# --------------------------------
text = "apple mango apple banana apple"

print(text.count("apple"))    # 3
print(text.count("banana"))   # 1
print()


# --------------------------------
# replace()
# Replaces one substring with another.
# --------------------------------
text = "I like Java"

print(text.replace("Java", "Python"))
print()


# --------------------------------
# len()
# Returns the total number of characters.
# --------------------------------
text = "Python"

print(len(text))      # 6
print()


# --------------------------------
# in operator
# Checks whether a substring exists.
# --------------------------------
text = "Python Programming"

print("Python" in text)   # True
print("Java" in text)     # False
print()


# --------------------------------
# not in operator
# Checks whether a substring does NOT exist.
# --------------------------------
print("Java" not in text)     # True
print("Python" not in text)   # False
print()