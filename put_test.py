import requests

user = {
    "name": "Yunus",
    "age": 24,
    "job": "AI Developer"
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/1",
    json=user
)

print(response.status_code)
print(response.json())