x = {1, 3, 4, 5, 1}
print(type(x))
print(x)

# Important: This syntax will create an empty dictionary and not an empty set
a = {}
print(type(a))

#Sets methods

# Creating an empty set
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6))

## Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

## Length of the Set
print(len(b)) # Prints the length of this set

## Removal of an Item
b.remove(5) # Removes 5 fromt set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)
# b.discard(4) #remove the 4 from the set
# b.clear() #clears the whole set
# del b deletes the set
print(b.pop())
print(b)
# sets are unordered so we cannot access an element like list or tuple
# print(b[1])

# it will remove the items that are comman
""" k1={"y","o","black"}
k2={"o","blue","p"}
k1.difference_update(k2)
print(k1) """

# tell about the subset and superset
""" k1={1,2,3,4,5}
k2={1,2,3,4,5,6,7,8}
print(k1.issubset(k2))
print(k2.issuperset(k1))"""

# return the union
""" k1 = {10, 20, 30, 40}
k2 = {50, 20, "10", 60}
k3 = k1.union(k2)
print(k3) """