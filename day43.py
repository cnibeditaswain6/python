#4. get() - returns the value of the key

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

print(student.get("name"))
print(student.get("age"))
print(student.get("subjects"))