import requests

response = requests.delete(
    "https://jsonplaceholder.typicode.com/users/1",
    
)

print(response.status_code)
print(response.json())