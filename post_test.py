import requests

user = {
    "name": "Yunus",
    "age": 24,
    "job": "AI Developer"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",

    json=user
)

print(response.status_code)
print(response.json())