animal = "Lion" #SyntaxError: missing quotation marks for string.
animal_type = "cub"
number_of_teeth = 16

full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth.")
#LogicalError: 'number_of_teeth' and 'animal_type' in the wrong position.
#LogicalError: missing full stop at the end of the sentence.
#SyntaxError: missing parentheses and missing f string.
print(full_spec) #SyntaxError: missing parentheses.
