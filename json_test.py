import json

user = {
    "name": "Yunus",
    "age": 24,
    "job": "AI Developer"
}

json_data = json.dumps(user)

print(json_data)
print(type(json_data))

python_data = json.loads(json_data)

print(python_data)
print(type(python_data))