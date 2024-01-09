#I am going to create a pattern using an if-else statement with a single
#foor loop! The pattern should be:
#*
#**
#***
#****
#*****
#****
#***
#**
#*

#First, we determine how many rows are needed and add them into a range.
#Then, we determine the highest amount of stars we need to print in one row.
#This will be for the first half of the pattern.
#In this case, the highest amount of stars needed in a row is 5 (highest star).

#Using an if-else statement, if the row number is <= 5, the star_count should
#equal to the row number, (e.g. 1 star on row 1, 2 stars on row 2, etc).
#Add a print statement to print the star_count on each row.

#Then, use an else statement for the rows that are bigger in value than the
#highest star.
#The star count starts to decrease by 1 and can use the formulae:
#star_count = 10(the total number of rows) - row_num (row number).
#Again, add a print statement to print the star_count on each row.

for row_num in range(1,10):
    if row_num <= 5:
        star_count = row_num
        print("*" * star_count)
    else:
        star_count = 10-row_num
        print("*" * star_count)