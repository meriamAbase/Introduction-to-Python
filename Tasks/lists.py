# =========== Python list Methods  ===========
# There are many useful built-in list methods available for you to use.
# Some other list methods can be found below:
#   extend()    - Adds all elements of a string/list to the another list   #Test this out!
#   insert()    - Inserts an item at the defined index
#   remove()    - Removes an item from the list
#   pop()       - Removes and returns an element at the given index        #Test this out!
#   index()     - Returns the lowest index where the element first appear. #Test this out!
#   count()     - Returns the count of the list                            #Test this out!
#   sort()      - Sorts items in a list in ascending order                 #Test this out!
#   reverse()   - Reverses the order of items in the list                  #Test this out!
#   append()    - Adds an element at the END of the list
#   copy.copy()      - Creates a shallow copy of the list
#   copy.deepcopy()  - Creates a copy of a nested list
#   clear()     - Used to remove all items from a list                     #Test this out!
#   sort()      - Sort a List in ascending, descending, or user-defined order
# alphabets = ['a','e','d','c','b'] 
# alphabets.sort() 
# print(alphabets)   #['a', 'b', 'c', 'd', 'e']
  
# random_numbers = [2,5,6,1,8,3] 
# random_numbers.sort() 
# print(random_numbers)       #[1, 2, 3, 5, 6, 8]
# #   min()       - Returns the smallest of the values in the list.
# numbers = [23,25, 65,21,98]
# print(min(numbers))   #21
# #   mox()       - Returns the biggest item in the list.



# # ===================Differnce between pop and remove===
# ===============
# # Remove is used when we have a name of a list item to remove it, e.g.:
# name_list = ['James', 'Molly', 'Chris', 'Peter', 'Kim']
# name_list.remove('Molly')
# print(name_list)

#  Whereas with pop, we use the index number to remove an item (or leave it empty to remove the last item)
# name_list = ['James', 'Molly', 'Chris', 'Peter', 'Kim']
# name_list.pop(1)
# print(name_list)

# # =======================del function=========================
# # Further to 'pop', which simply can only remove one function at a time, we can
# #  use 'del' to delete multiple items from a list.
# # Example 1: Deleting 1 item
# random_list = ['banana', 'apple', 'peach', 'plum', 5, 6, 7]
# del random_list[1]      #['banana', 'peach', 'plum', 5, 6, 7]
# print(random_list)
# # Example 2: Deleting mutliple items
# del random_list[1:4] #Deleting items in index 1, 2 and 3
# print(random_list)      #['banana', 6, 7]
# # And finally, to simply delete the whole list:
# del random_list
# # When atttempting to print 'random_list', we can see that we get a 'NameError'
# # since it no longer exists!

# ================== Checking if Something is in a List ==================
# You can simply use an if statement to check if a certain item is in a list.
# grocery_list = ['Bread', 'Milk', 'Butter', 'Cheese', 'Cereal']
# # Preferred option and shorter code:
# if 'Apples' in grocery_list:
#     print('The item Apples was found in the list grocery_list')
# else:
#     print('The item Apples was not found in the list grocery_list')
        
# # This is a much quicker way than looping through all the items, such as if you did:
# for item in grocery_list:
#     if item == 'Apples':
#         print('The item Apples was found in the list grocery_list')

# # =====================Nested lists=======================
# # We can nest lists into other lists, for example:
# a = [1,2,3]
# b = ["a", "b", "c"]
# c = [a, b, 'random word', 5]
# print(c)        #[[1, 2, 3], ['a', 'b', 'c'], 'random word', 5]
# # We can also remove nested lists using the .remove() function followed by which list or item you wish to remove.
# c.remove(b)
# print(c)        #[[1, 2, 3], 'random word', 5]

# # ==================Replacing elements in a list==================
# # We can recall a list with an index number to replace a value! e.g:
# name_list = ['James', 'Molly', 'Chris', 'Peter', 'Kim']
# name_list[4] = 'Billy'
# print(name_list)    #['James', 'Molly', 'Chris', 'Peter', 'Billy']
# # To take this one step further, we can also call a range of indexes followed by 
# # their replacements to replace more than one item at a time, e.g:
# name_list[0:2] = ['Jill', 'Milly', 'Carter']
# print(name_list)    #['Jill', 'Milly', 'Carter', 'Chris', 'Peter', 'Billy']




# =====================Copying Lists=======================
# import copy

# # Using a slice '[:]' for a single list creates a new copy for b (and a different ID address!
# # we can also use the copy.copy() function to copy a single list
# # We can also name the list followed by the index we wish to change.
# a = [1, 2, 3]
# b = a[:]
# c = copy.copy(a)
# b[1] = 10
# c[1] = 12

# print(a)
# print(b)
# print(c)

# # However if we simply made b = a,this would give them the same ID address and would therefore be linked.
# # We can see this in the following example.
# a = [1, 2, 3]
# b = a
# a[0]= 10
# print(b)

# # =========================Copying in 2D lists=============================
# # The above functions do not work the same on 2d lists.
# # If we have a 2d list, then defining b as 'a[:]' will no longer create a new ID, if will have the same.
# # And also, using 'c = copy.copy(a)' will also create the same ID! Instead, for 2d lists we use:
# # 'c= copy.deepcopy(a)' to run a 'deep copy' of the list and including any lists within the list!

# a = [[1, 2, 3], [4, 5, 6]]
# b = a[:]
# c = copy.deepcopy(a)
# b[0][1] = 10
# c[0][1] = 12

# print(a)
# print(b)
# print(c)