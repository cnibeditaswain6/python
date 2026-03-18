#Q. Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

#1st possible solution
# values = {9, "9.0"} 
# print(values)

#2nd solution - according to que

values = {
    ("float", 9.0),
    ("int", 9)
}

print(values)

