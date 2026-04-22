# dictionary = key:value pairs (real dict jaisa)
student = {
    "name": "Shreyansh",
    "age": 18,
    "course": "Mechatronics"
}

print(student["name"])       # direct access
print(student.get("age"))    # safe access (error nahi deta)
student["university"] = "ggg"  # naya key add karo
print(student)