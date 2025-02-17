dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "painting"],
    "education": {
        "degree": "Bachelor's",
        "major": "Computer Science"
        # Additional education details can be added here
    }
}

# print(dictionary, type(dictionary))

# print(dictionary.keys())

print(dictionary["age"])

print(dictionary.get("name"))

dictionary["name"] = "Mohammad Abdullah"

print(dictionary.get("name"))

dic = {}

print(type(dic))