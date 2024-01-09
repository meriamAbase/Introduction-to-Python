#First, we need to ask the user for the following:
#Name, age, house num and street name.
name = input("What is your Full name? ")
age = input("How old are you? ")
house_num = input("What is your house number? ")
street_name = input("What is your street name? ")

#Next, we will print these all in a single sentence on one line using an f function.
print(f"This is {name}. They are {age} years old and lives at house number {house_num} on {street_name}.")