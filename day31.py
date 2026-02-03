 # List Slicing

marks = [85,94,76,63,48]
print(marks[1:])

# #List Methods
# #1. Append - Adds one element at the end.

list = [2,1,3]
list.append(4)
print(list)

# #2. Sorting
# # Sorting(ascending order)

a = [3,4,5]
a.append(8)
print(a.sort())
print(a)

# #Sorting(decending order)- reverse = True

n = [4,7,9,3]
print(n.sort(reverse = True))
print(n)

# # sorting characters

list = ['u', 'b', 'n', 'e', 'g', 'f', 'a']
print(list.sort())
print(list)


list = ['u', 'b', 'n', 'e', 'g', 'f', 'a']
print(list.sort(reverse = True))
print(list)


# #3. Reverse

char = ['u', 'b', 'n', 'e', 'g', 'f', 'a']
char.reverse()
print(char)


#4. Insert - Insert element at index

n = [2, 5, 4,]
n.insert(5, 3)
print(n)


#5. Remove - removes first occurrence of element.

list = [1, 2, 3, 1, 5]
list.remove(1)
print(list)

#6. Pop - remove element at index.

list = [1, 2, 3, 1, 5]
list.pop(3)
print(list)
