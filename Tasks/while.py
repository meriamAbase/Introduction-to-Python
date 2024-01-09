#We are creating a programm that asks users to enter a number.
#The program should continue to ask users for a number until they enter
#the value '-1'

num = int(input("Enter a number: "))
while num > -1 or num < -1:
    num = (int(input("Enter a number:")))
    if num == -1:
        break
    
#We have to remember to change num in the while-loop so that the system
#repetedly asks the user for a new number!