#3. items() - returns all the key value pairs as tuples.

student = {
    "name" : "Nibedita Swain",
    "age" : 22,
    "subjects" : {
        "dsa" : 54,
        "ai" : 97,
        "cd" : 76,
        "se" : 55,
    }
}

print(student.items())
print(list(student.items()))