from functools import reduce



# A. Creating & Indexing Lists

fruits = ["apple","mango","banana"]
# print(fruits[0]);
# print(fruits[-1])


# Slicing Lists

# numbers = [0,1,2,3,4,5,6,7,8,9]

# print(numbers[1:4])
# print(numbers[:4])
# print(numbers[4:])


# iterating list

# for i in numbers:
#     print(i)



# Modifying Lists

# fruits.append("orange")
# print(fruits)


# fruits.insert(1,"papaya")
# fruits.remove("banana")
# fruits.pop(2)               # Remove by index
# print(fruits)

# fruits.sort()               # Sort alphabetically
# print(fruits)



#       ***********************************************     Tuples    ****************************************

# coordinate = (1,0)
# print(coordinate[1])

# Tuples don't change


#       ***********************************************     Dictionaries    ****************************************

# Person={"name" :"prem",
#         "age":51,
#             "city": "Mumbai"
# }

# print(Person["name"])       # Access directly → Prem
# print(Person.get("email"))  # Safer → returns None if key doesn't exist

# for key, value in Person.items():
#     print(key ,":", value)

# print(Person.keys())   # Just keys
# print(Person.values()) # Just values


# # Modyfying

# # C. Modifying

# Person["age"] = 26         # Change value
# Person["email"] = "prem@example.com"  # Add new key-value pair
# del Person["city"]         # Remove a key-value pair
# print(Person)


# # SET

# nums = {1, 2, 3, 3, 4}
# print(nums)  # {1, 2, 3, 4} → duplicates removed automatically

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# print(set1.union(set2))        # Combine → {1, 2, 3, 4, 5}
# print(set1.intersection(set2)) # Common → {3}
# print(set1 - set2)             # Difference → {1, 2}


# # String

# name = "Prem"
# age = 25

# print(f"My name is {name} and I am {age} years old.")  # f-string
# print("My name is {} and I am {} years old.".format(name, age))  # format method

# sent = "My name is Prem"
# words = sent.split()
# join = "--".join(words)
# print(words)
# print(join)



# # Change CASE

# text = "Hello world"
# print(text.upper())    # HELLO WORLD
# print(text.lower())    # hello world
# print(text.title())    # Hello World
# print(text.replace("world", "Python"))  # Hello Python


# numbers = []
# for i in range (1,6):
#     numbers.append(i*2)

# print(numbers)


#       *************************************   lambda functions    *********************************

# Lambda function
# add_lambda = lambda x, y: x + y

# print(add_lambda(3, 5)) # 8


# points = [(2, 3), (1, 5), (4, 1)]
# points.sort(key=lambda p: p[0])  # Sort by second value
# print(points)  # [(4, 1), (2, 3), (1, 5)]


#   **********************************************  MAP        ************************************

numbers= [1,2,3,4,5,6]

# def sq(x):
#     return x**2

# square = list(map(sq, numbers))
# print(square)
# sqr = list(map(lambda x: x**2,numbers))
# print(sqr)


# ************************************************  Filter   ***************************************
# filter(function, iterable)
# function → must return True/False

# Only elements with True are kept.

# def ev(x):
#     return x%2 == 0
# even = list(filter(ev,numbers))
# evn = list(filter(lambda x : x%2 == 0, numbers))
# print(even)
# print(evn)


#        ************************************************  Reducer   **************************************

# from functools import reduce
# reduce(function, iterable, initial_value(optional))
# function → takes two inputs, combines them.

# Keeps applying until only one result remains.



# total = reduce(lambda x, y: x+y, numbers)
# print(total)

# ************************************************  Enumerate & Zip   ***********************************

# fruits = ["apple", "banana", "cherry"]

# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# names = ["Prem", "Soham", "Adi"]
# scores = [90, 85, 92]

# for name, score in zip(names, scores):
    # print(f"{name} scored {score}")



#  ********************************************* Error Handling   ***********************************

# try:
#     numbers= int(input("enter num : "))
#     print(10/numbers)
# except ValueError:
#     print("enter correct value")
# except ZeroDivisionError:
#     print("num cannot be zero")
# finally:
#     print("this will alway run")


# *************************************************  6️⃣ Modules & Packages  ***********************************

import math

print(math.pow(4,2))

# # *************************************************  Making your own module  ***********************************

# Creating Your Own Module

# 📁 mymath.py

# def add(a, b):
#     return a + b


# 📁 main.py

# import mymath

# print(mymath.add(5, 3))  # 8


# Why this way?

# Keeps code organized into separate files.

#    *********************************************** Packages  **********************************

from mypackage import mathutils

print(mathutils.add(5,7))




# ✅ Summary:

# List Comprehensions → short, clean list creation.

# Lambda → quick one-line functions.

# Map, Filter, Reduce → functional data processing.

# Enumerate, Zip → clean looping.

# Error Handling → avoid crashes.

# Modules & Packages → organize code.