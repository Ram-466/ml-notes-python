student = {
    "name": "Ram",
    "age": 24,
    "field": "Machine Learning"
}

print("Name:", student["name"])

student["age"] = 25
student["country"] = "USA"

print("Updated dictionary:", student)

for key, value in student.items():
    print(key, "->", value)
