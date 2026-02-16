#2. values() - collection of all the values in the dictionary(returns all values).

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

print(student.values())
print(list(student.values()))