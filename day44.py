#5. update() - inserts the specified items to the dictionary.

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

student.update({"city" : "delhi"})
print(student)
print(list(student))