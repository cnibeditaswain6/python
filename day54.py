#Q. WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# start with an empty dictionary & add one by one.
# use subject name as key & marks as value.

marks = {}

a = int(input("Enter DSA Marks : "))
marks.update({"DSA" : a})

b = int(input("Enter SE Marks : "))
marks.update({"SE" : b})

c = int(input("Enter CD Marks : "))
marks.update({"CD" : c})

print(marks)











    