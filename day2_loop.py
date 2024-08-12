# """"
# Introduction to python

# Python is a high-level programming language for general-purpose programming. It is an open source, interpreted, objected-oriented programming language. Python was created by a Dutch programmer, Guido van Rossum. The name of Python programming language was derived from a British sketch comedy series, Monty Python's Flying Circus. The first version was released on February 20, 1991.
# """
# """
# Data types

# """
# print("Hello world")
# firstname = input("Enter your Firstname: ")
# lastname= input("Enter your Lastname: ")
# print("Hello " + firstname + lastname)









# # Assignment

# from datetime import datetime

# firstname = input("Enter your Firstname: ")
# lastname= input("Enter your Lastname: ")
# year_of_birth = abs(int(input("Enter your birth year: ")))
# current_year = datetime.now().year
# age = current_year - year_of_birth
# print("Hello " + firstname + lastname + " you are " + str(age) + "  years old")
#


# FOR LOOP
fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)


# Loop through the letters in the word "banana":
# looping through a string
# for x in "banana":
#     print (x)



# break statment: With the break statement we can stop the loop before it has looped through all the items:

# for x in fruits:
#     print(x)
#     if x == "banana":
#         break

# Exit the loop when x is "banana", but this time the break comes before the print:
# for x in fruits:
#     if x == "banana":
#         break
#     print(x)


# continue statement: With the continue statement we can stop the current iteration of the loop, and continue with the next
# for x in fruits:
#         if x == "banana":
#             continue
#         print(x)


# The range() Function

# To loop through a set of code a specified number of times, we can use the range() function,

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# for x in range(6):
   # print(x) #prints 0, 1, 2, 3, 4, 5

# for x in range(2, 6):
#     print(x) #prints 2, 3, 4, 5

# 

# food = ["egg", "banana", "peanut", "beske"]
# for x in  food:
#    if x == "egg":
#       print (x)
#       break

   # food = ["egg", "banana", "peanut", "beske"]
   # for x in  food:
   #    print (x)
   # if x == "egg":
   #    break


#while loop
# i = 3
# while i < 6:
#     print (i)
#     i+=1

   


# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i  +=1 

# i = 0
# while i < 20:
#     print(i)
#     if i == 13:
#         break
#     i += 1

# i = 0
# while i < 20:
#   i += 1
#   if i <= 15:
#    continue
#   print(i) 
# print(i) #prints final value of i

# i = 5
# while i < 6: 
#   print(i)
#   i += 1
# else:
#   print("i is no longer equal to 1")

# Exercise
import random

n = random.randrange(0, 6)
attempts = 5
attempts_made = 0
guess = int(input("make a guess by typing a number: "))
while attempts > 0:
  attempts_made += 1
  if guess < n:
    print(f"Number too low")
  elif guess < n:
    print(f"number too high") 
  else:
    print("You guessed right")
  break
# else:
#   print("you have no attempts left")
remaining_attempts = attempts - attempts_made
if remaining_attempts > 0:
  print(f"you have {remaining_attempts}{f"remaining_attempts" if remaining_attempts > 1 else 'remaining_attempt'} left") 
else:
  {"you have no attempts left"}