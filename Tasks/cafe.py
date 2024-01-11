# Scenario: Imagine you own a cafe. Create a program that calculates your total
# stock value.

# First, create a menu with all the items you sell.
menu = ["Cake", "Coffee", "Full English Breakfast", "Pancakes"]


# Create a dictionary called 'stock' which should contain the stock value for
# each item.
# Remember to make each item from the menu as the key so we can refer to the
# stock by calling the keys in the dictionary! (key: value) -> (menu: stock)
stock = {menu[0]:8, menu[1]:11, menu[2]:6, menu[3]:7}


# Creat a dictionary called 'price' which should contain the prices for each
# item on the menu. Again, follow the same principle above for the dictionary.
price = {menu[0]:3.99, menu[1]:1.99, menu[2]:8.99, menu[3]:6.99}


# To calculate the total stock value, first create an empty variable.
# Use a for-loop to mulitply each item's stock by the price
# (stock[item] * price[item]).
# This is then added to the total of the empty variable ('total_stock').

# Note: for each item in the menu, we use the 'stock' and 'price' dictionaries
# linked to the items, to add the correct values for each iteration.
total_stock = 0
for item in menu:
    total_stock += stock[item] * price[item]
    
# Finally, print out the results of the calculation.
print(f"The total stock value is £{total_stock}")