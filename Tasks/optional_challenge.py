# print"Calculating your number * your number." #Syntax error: missing parentheses.
# num = int(input("Enter a name: ")) #LogicalError: print statement does not make
# #sense. We are asking for an integer!
# sum = number * num #RuntimeError: 'number' not defined.
# print("The answer is " str(sum)) #SyntaxError: missing '+' sign after string.

print("Calculating your number * your number.") 
num = int(input("Enter a number: "))
sum = num * num 
print("The answer is " + str(sum))