import copy

# Using a slice '[:]' for a single list creates a new copy for b (and a different ID address!
# we can also use the copy.copy() function to copy a single list
# We can also name the list followed by the index we wish to change.
a = [1, 2, 3]
b = a[:]
c= copy.copy(a)
b[1] = 10
c[1] = 12

print(a)
print(b)
print(c)

# However if we simply made b = a,this would give them the same ID address and would therefore be linked.
# We can see this in the following example.
a = [1, 2, 3]
b = a
a[0]= 10
print(b)

# =========2D lists============
# The above functions do not work the same on 2d lists.
# If we have a 2d list, then defining b as 'a[:]' will no longer create a new ID, if will have the same.
# And also, using 'c= copy.copy(a)' will also create the same ID! Instead, for 2d lists we use:
# 'c= copy.deepcopy(a)' to run a 'deep copy' of the list and including any lists within the list!

a = [[1, 2, 3], [4, 5, 6]]
b = a[:]
c= copy.deepcopy(a)
b[0][1] = 10
c[0][1] = 12

print(a)
print(b)
print(c)