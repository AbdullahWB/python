#set = {} # empty set not defined by {}
s = set() # empty set  defined by like that
print(type(s))

duplicate_set = {1, 2, 2, 3, 3, 4}

print(duplicate_set) # it will remove the duplicate values

my_set = {1, 2, 3}
my_set.add(4)
print(my_set) 

my_set.update([5, 6, 7])
print(my_set)

my_set.remove(4)
print(my_set)

my_set.discard(100)  # No error
print(my_set)

removed_element = my_set.pop()
print(removed_element) 
print(my_set)