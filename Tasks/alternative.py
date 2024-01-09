#For this task, I am creating a program which alternates between making a letter
# uppercase, making the next lowercase, and so on. The steps are as follows:

# First, add a sentence into a variable to test on.

# Then, create an empty variable to store data for each loop.
# Create a for-loop and define the range you would like to check.
# Use the 'len' function to fetch the length of your chosen variable.

# If the index is divisble by 2, make the letter uppercase,
# else, make the letter lowercase.
# The 'result' variable is then updated with each loop.
# And finally, print the results.

# Here is an example with a string.
alternate = "I hope this works"

result = ""
for index in range(len(alternate)):
    if index % 2 == 0:
        result = result + alternate[index].upper()
    else:
        result = result + alternate[index].lower()

print(result)

# The same code can be used when suggesting for user input!
# Simply adjust the variable to request an input. 
# In this example, the 'len' function will personalise according to the 
# sentence given.
user_input = input("Enter a sentence: ")

result = ""
for index in range(len(user_input)):
    if index % 2 == 0:
        result = result + user_input[index].upper()
    else:
        result = result + user_input[index].lower()
    
print(result)


# Now, using the same string in the example above, we are going to make each
# alternate word uppercase and the other words lowercase.

# First, use .split() to create seperate indexes for each word.
# Then, repeat the same process as above, this time making sure to add '+ " "'
# at the end of each loop option so that the indexed words have empty 
# characters between them for readability.

alternate = alternate.split()

result = ""
for index in range(len(alternate)):
    if index % 2 == 0:
        result = result + alternate[index].upper() + " "
    else:
        result = result + alternate[index].lower() + " "
print(result)  

# Again, we can use the same code and adjust it if we require user input
# (as shown below).  
user_input1 = input("Enter a sentence of at least four words: ") 
user_input1 = user_input1.split()

result = ""
for index in range(len(user_input1)):
    if index % 2 == 0:
        result = result + user_input1[index].upper() + " "
    else:
        result = result + user_input1[index].lower() + " "
print(result)  

