print ("Welcome to the error program.") #SyntaxError: Missing parentheses.
print ("\n") #SyntaxError: Indentation error and missing parentheses.

#Syntax Error on next 3 lines: Indentation error.
age_str = "24" #RuntimeError: This will not convert to an integer with words.
#SyntaxError: only one equals sign is needed to create a variable.
age = int(age_str) 
print(f"I'm {age} years old.") #LogicalError: No spacing, easier with an
#f string.

#Syntax Error on next 2 lines: Indentation error.
years_from_now = 3 #SyntaxError: quote marks turns number into a string.
#and will not create a sum for 'total_years'.
total_years = age + years_from_now

print (f"In three years, I will be {total_years} years old.") #RuntimeError:
#'answer_years' is not defined. Use f string and add correct variable.
#SyntaxError: No parentheses. 
#LogicalError: Print statement doesn't make sense. It had no spacing either.

total_months = total_years * 12 #RuntimeError: 'total' not defined.
print ("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old.")
#SyntaxError: missing parentheses.
#RuntimeError: 'total_months' needs to be a str().
#LogicalError: total_months only calculates the total months for 27 years,
#forgetting to add the 6 months!