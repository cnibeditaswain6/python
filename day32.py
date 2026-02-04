# Tuples in Python - A built-in data type that lets us create immutable sequences of values.

tup = (2, 1, 3, 1)
print(type(tup))
print(tup[0])


# Tuple Methods

#1. index - returns index of first occurence.

tup = (1, 2, 3, 4, 5)
print(tup.index(3))
 

#2. Count - counts total occurrences

tup = (1, 2, 3, 5, 3, 4, 3, 3)
print(tup.count(3))