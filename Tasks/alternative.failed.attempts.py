#For this task, I am creating a program which alternates between capitalising 
#one letter, and making the next lowercase, and so on.

# First attempt
alternate = "I hope this works"

for char in alternate:
    if char % 2 == 0:
        alternate = alternate.upper()
    else:
        alternate = alternate.lower()
        print(alternate)    

#After researching and 1 week later... 

# Second attempt

# First we create an empty variable to store data for each loop.
# Then, we start the for-loop and define the range we would like to check.
# We use the 'len' function to fetch the length of our chosen variable.

# Then, we simply say, if the index is divisble by 2, make the letter uppercase,
# else, make the letter lowercase.
# And finally we print the 'result' variable we created.

# Here is an example with a string.
alternate = "I hope this works"

result = ""
for index in range(len(alternate)):
    if index % 2 == 0:
        result = result + alternate[index].upper()
    else:
        result = result + alternate[index].lower()

print(result)

# We can use the same code when suggesting for user input!
# Simply adjust the variable to request an input. 
# In this example, the 'len' function will personalise according to the 
# sentence given.
alternate = input("Enter a sentence: ")

result = ""
for index in range(len(alternate)):
    if index % 2 == 0:
        result = result + alternate[index].upper()
    else:
        result = result + alternate[index].lower()
    
print(result)
