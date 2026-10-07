import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    response.raise_for_status()

    users = response.json()

    for user in users:
        print(user["name"], "-", user["email"])

except requests.exceptions.RequestException as e:
    print("API isteğinde hata oluştu:", e)