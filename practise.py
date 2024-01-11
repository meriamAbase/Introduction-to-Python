#===========While loops===========
# sum = 0
# while sum <10:
#     sum+=2
#     print(sum)
# #This adds 2 each time until loop is met.



# sum1 = 0
# i = 2
# while sum1 <= 10:
#     sum1 += i
#     i+= 2
#     print(sum1)
# #This on the other hand, increases i by 2 each time and therefore adds 2 first, and then 4, and then 6 etc etc until the loop is met.

# i = 0 
# while i <10:
#     i+=1
#     print(i)
#     #This prints numbers 1 to 10 because the last successful number which is less than 10, gets 1 added to it before it prints.

#break - breaks the loop once a certain condition is met and it stops completely.
#continue - checks for certain values and removes these from the while loop and continues for the rest of the values.

#===========For loops=============
#for loops have a variable (such as i) which takes the values
#from a sequence, this can be each character of a letter or, if more than one word/num
#is seperated by a comma, then each word/num is char 1, char2 etc.
#we can also use the word 'range' for numbers to avoid tyoing them all one by one:
#e.g.:
#for i in range(1,10): [start num is inc, end num is not]
    #print(i), this will print numbers 1 to 9.
#You can use an if statement within for loops. e.g:
#The following will print numbers 6 to 9:
#for i in range(1,10):
    #if 1 > 5:
    #print(i)

#Example of a for-loop within an if-loop:
# num_list = [1, 2, 3, 4, 5]
# found = False
# num = int(input("Input a number from 1 to 10 and find out if its in our list: "))
# if num<1 or num>10:
#     print("Num out of range.")
# else:
#     for number in num_list:
#         if num == number:
#             found = True
#             break #(Is this neccesary? It works without it.)*
#     print(f"List contains {num}: {found}")
#In this example, 'num out of range' covers invalid numbers,
#whilst the for loop checks each number in the list and if num== a number in
#the list, in turns found -> True!
#If it is false (nums 6 to 10) it will keep found False.
#Then the print statment prints the number chosen and if it is True or False!
#* To add to this, this break statement is super important when using a for loop
#to input data from another file as the file could be really big and it will 
#break once the condition has been found, scanning the rest is not needed. We 
#don't know how much data is in the files and if there are any infinite loops
#and therefor is very important to add this when reading a file.

#Nested loop program that prints out the timestables!
# for x in range(1,6):
#     for y in range(1,6):
#         print(f"{x} x {y} = {x*y}")
#     print("")

#=====Practising printing patterns=====

#First attempt
# for i in range(5):
#     for j in range(i+1):
#         print("*", end="")
#     print()
# for i in range(4):
#     for j in range(4-i):
#         print("*", end="")
#     print()

#Second attempt with google example.
# row_count = 5
# start = 1
# end = (2 * row_count)
# for row_number in range(start, end):
#     if row_number <= row_count:
#         star_count = row_number
#     else:
#         star_count = end - row_number
#     for i in range(star_count):
#         print("*", end=" ")
#     print()

#Final correct method after lecture help!:
# for row_num in range(1,10):
#     if row_num <= 5:
#         star_count = row_num
#         print("*" * star_count)
#     else:
#         star_count = 10-row_num
#         print("*" * star_count)

#=====Practising def with different arguments=====
#Positioning argument
# def person (name, age):
#     print(name)
#     print(age)
    
# person ("Meriam", 29)

#Keyword argument
# def person (name, age):
#     print(name)
#     print(age)

# person(age = 29, name = "Meriam")

#Default variable
# def person (name, age=18):
#     print(name)
#     print(age)

# person("Meriam")

#Variable length argument
# def sum(*b):
#     c = 0
#     for i in b:
#         c = c + i 
#         print(c)

# sum(1,2,3,4,5)
#This seems to print the 1st number, and then the 1st and 2nd added together
#on the second line, then that total plus the 3rd number on the third line etc.

#Keyword variable length argument
# def person (name,**data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)
        
# person("Meriam", Age=29, Birth="Bolton", Mob=447508644727)

#=============Loops=============
#Printing the same thing multiple times using a 
#temporary variable such as i within a for loop:
# for i in range(0,3):
#     print("Hello You.")
    
#Printing the count next to each word using enumarate.
#(And starting with number 1 as shown next to enumerate(wizards,1))
# wizards = ["Harry", "Ronald", "Hermione", "Dumbledore", "Malfoy"]
# for count,wizard in enumerate(wizards,1):
#     print(count,wizard)

#Printing statements next to each list item.
# wizards = ["Harry", "Ronald", "Hermione", "Dumbledore", "Malfoy"]
# for pos,wizard in enumerate(wizards,1):
#     if wizard in ["Harry", "Ronald", "Dumbledore"]:
#         print(f"You're a wizard {wizard}!")
#     elif wizard in ["Hermione"]:
#         print(f"You're a mudblood {wizard}!") 
#     else:
#         print(f"{wizard}, I smell a slytherin")   
#     print("Hello") #Prints "Hello" after each loop!

#=======String Handling=======
# practise = "The$brown$fox$fell$in$love$with$the$white$rabbit."
# practise = practise.replace('$', ' ')
# print(practise)
# practise = practise.split()
# print(practise)
# practise.pop()
# print(practise)
# practise.append('rabbit')
# print(practise)
# practise.insert(0,'Happily,')
# print(practise)
# practise.pop(0)
# print(practise)
# practise.remove('brown')
# print(practise)
# practise = " ".join(practise)
# print(practise)

# practise = " ".join(practise)
# print(practise)
# practise = practise.upper()
# print(practise)

# string = "      Testing, testing, 1, 2, 3,   "
# print(string)
# string = string.strip()
# print(string)
# string = string.strip(',')
# print(string)


#  --- Multiple input example for valid full name

# full_name = input("Enter your full name: ")

# valid_name = False
# while not valid_name:
#     if ' ' not in full_name:
#         full_name = input("Please re-enter your full name: ")
#     else:
#         valid_name = True

"""
Challenge 1:
Create a for-loop that takes a base 
number and an exponent number and 
returns the calculation.
"""

# Challenge 1 : 2 * 5 = 32

# user_base = int(input("Enter base value: "))
# user_expo = int(input("Enter exponent value: "))

# total = 1

# for value in range(user_expo):
#     # print(f"{total} * {user_expo}")
#     total *= user_base
#     # print(total)

# print(f"{user_base} to the power of {user_expo} is: {total}")

"""
Challenge 2
Create a for loop that takes a list of numbers. 
Return the largest number in the list.
"""
# list_of_numbers = [-1, -90, -23, -678, -101]
# largest_num = list_of_numbers[0]
# print(largest_num)

# for num in list_of_numbers:
#     if num >= largest_num:
#         largest_num = num
        
# print(f"The largest number in the list is: {largest_num}")

"""
Challenge 3
Create a for loop that takes a list of numbers and 
returns the smallest number in the list.
"""
# # Challenge 3
# list_of_numbers = [12, 34, 5, 678, 101]
# smallest_num = list_of_numbers[0]

# for num in list_of_numbers:
#     if num <= smallest_num:
#         smallest_num = num

# print(f"The smallest number in the list is: {smallest_num}")

"""
Challenge 4

Create a for loop that takes a list and returns the difference between
the biggest and smallest numbers.
"""

# # Challenge 4
# list_of_numbers = [10, 4, 1, 4, -10, -50, 32, 21]
# smallest_num = list_of_numbers[0]
# largest_num = list_of_numbers[0]

# for num in list_of_numbers:
#     if num <= smallest_num:
#         smallest_num = num
#     if num >= largest_num:
#         largest_num = num

# value_difference = largest_num - smallest_num
# print(f"The smallest number is: {smallest_num} \nThe largest number is: {largest_num} \n The difference is: {value_difference}")

"""
Challenge 5
Create a for loop that takes a list 
and returns the sum of all numbers in the list.
"""
# Did this one myself, yay :)
# sum=0
# list_of_numbers = [10, 4, 1, 4, -10, -50, 32, 21]
# for num in list_of_numbers:
#     sum += num
#     # print(sum)
# print(f"The sum is {sum}")    

# sum=0
# list_of_numbers = [1, 2, 3, 4, 5]
# for num in list_of_numbers:
#     sum += num
#     # print(sum)
# print(f"The sum is {sum}")    

#==========While loop=========
# # Example of a while loop that continues until loop is False
# found_mikie = False
# while not found_mikie:
#     print("My friend's name is Andrew.")
#     your_friend = input("Provide your friend's name: ").lower()
#     if your_friend == "mikie":
#         found_mikie = True

# for first_iter in range(0, 3):
#     for inner_iter in range(0, 6): 
#         print(f"{first_iter} : {inner_iter}")
#     print()
    

# # Multiplication table
# user_num = int(input("Enter a number: "))
# for x in range(1, 11):
#     print(f"{x} x {user_num} = {x * user_num}")
# count = 1

# === Task 7 - Repeat input until stop with while-loop ===
"""
ask the user to press enter or enter the word "stop"
while the user has not entered "stop"
    print "Hello"
    ask the user to press enter or enter the word "stop"
"""
# user_input = input("Please press enter or enter the word 'stop': ")

# while user_input.lower() != "stop":
#     print("Hello")
#     user_input = input("Please press enter or enter the word 'stop': ")


# # === Example 3: Sum of Squares ===
# # -- for loop option --
# numbers = [1, 2, 3, 4, 5]

# sum_of_squares = 0

# for num in numbers:
#     sum_of_squares += num ** 2
#     print(sum_of_squares)

# print(f"The sum of squares is: {sum_of_squares}")


# === Example 4: User Input Validation
# # -- while loop option --

# user_input = input("Enter a positive integer: ")
# while not user_input.isdigit() or int(user_input) <= 0:
#     print("Invalid input. Please enter a positive integer.")
#     user_input = input("Enter a positive integer: ")

# # At this point, user_input is a valid positive integer
# print(f"You entered: {user_input}")

# # Example of name def
# def name(first: str, last: str):
#     first = first.upper() # Append `()` to call `upper` method.
#     last = last.upper()   # Replaced `,` with `.`.
#     print("HELLO", first, last)

# name('Meriam', 'Abase')
