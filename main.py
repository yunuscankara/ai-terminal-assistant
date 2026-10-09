import requests
import json


def get_users():
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users"
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException:
        print("Program Cevap vermiyor")
        return []


def find_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user

    return None


def show_email():
    users = get_users()

    try:
        user_id = int(input("Kullanıcı ID: "))
    except ValueError:
        print("ID sadece sayı olmalıdır.")
        return

    user = find_user(users, user_id)

    if user:
        print("Email:", user["email"])
    else:
        print("Kullanıcı bulunamadı.")


def show_users():
    users = get_users()

    for user in users:
        print(user["name"])


def show_user():
    users = get_users()

    try:
        user_id = int(input("Kullanıcı ID: "))
    except ValueError:
        print("ID sadece sayı olmalıdır.")
        return

    user = find_user(users, user_id)

    if user:
        print("İsim:", user["name"])
        print("Email:", user["email"])
        print("Telefon:", user["phone"])
        print("Şehir:", user["address"]["city"])
    else:
        print("Kullanıcı bulunamadı.")


def show_help():
    print("=== AI Terminal Assistant ===")
    print("Komutlar:")
    print("users - Kullanıcıları getir")
    print("user - Kullanıcı bilgisi getir")
    print("email - Kullanıcı emailini getir")
    print("add - Yeni kullanıcı ekle")
    print("delete - Kullanıcı sil")
    print("update - Kullanıcı güncelle")
    print("forget - Hafızadan bilgi sil")
    print("remember - Bilgi kaydet")
    print("memory - Hatırlanan bilgileri göster")
    print("help - Komutları göster")
    print("q - Çıkış")



def add_user():
    name = input("İsim: ")

    try:
        age = int(input("Yaş: "))
    except ValueError:
        print("Yaş sadece sayı olmalıdır.")
        return

    job = input("Meslek: ")

    user = {
        "name": name,
        "age": age,
        "job": job
    }

    try:
        response = requests.post(
            "https://jsonplaceholder.typicode.com/users",
            json=user
        )

    except requests.exceptions.RequestException:
        print("Program Cevap Vermiyor")
        return

    if response.status_code == 201:
        print("Kullanıcı başarıyla eklendi")
        print(response.json())
    else:
        print("Kullanıcı eklenmedi")


def delete_user():
    try:
        user_id = int(input("Kullanıcı ID: "))
    except ValueError:
        print("ID sadece sayı olmalıdır.")
        return

    try:
        response = requests.delete(
            f"https://jsonplaceholder.typicode.com/users/{user_id}"
        )

    except requests.exceptions.RequestException:
        print("Program Cevap Vermiyor")
        return

    if response.status_code == 200:
        print("Kullanıcı başarıyla silindi")
    else:
        print("Kullanıcı silinemedi")


def update_user():
    try:
        user_id = int(input("Kullanıcı ID: "))
    except ValueError:
        print("ID sadece sayı olmalıdır.")
        return

    users = get_users()
    user = find_user(users, user_id)

    if not user:
        print("Kullanıcı bulunamadı.")
        return

    name = input("Yeni isim: ")

    try:
        age = int(input("Yaş: "))
    except ValueError:
        print("Yaş sadece sayı olmalıdır.")
        return

    job = input("Meslek: ")

    user = {
        "name": name,
        "age": age,
        "job": job
    }

    try:
        response = requests.put(
            f"https://jsonplaceholder.typicode.com/users/{user_id}",
            json=user
        )

    except requests.exceptions.RequestException:
        print("Program Cevap Vermiyor")
        return

    if response.status_code == 200:
        print("Kullanıcı başarıyla güncellendi")
        print(response.json())
    else:
        print("Kullanıcı güncellenmedi")
        print("Status Code:", response.status_code)
        print("Response:", response.text)




def load_memory():
    with open("memory.json", "r") as file:
        memory = json.load(file)
        return memory


def save_memory(memory):
    with open("memory.json", "w") as file:
        json.dump(memory, file)

def remember():
    memory = load_memory()

    note = input("Hatırlanacak bilgi: ")

    memory["notes"].append(note)

    save_memory(memory)

    print("Bilgi kaydedildi.")

def show_memory():
    memory = load_memory()
    notes = memory["notes"]

    if not notes:
        print("Henüz kayıtlı bilgi yok.")
    else:
        print("\nKayıtlı bilgiler:")

        for index, note in enumerate(notes, start=1):
            print(f"{index}. {note}")


def forget():
    memory = load_memory()
    notes = memory["notes"]

    if not notes:
        print("Silinecek bir bilgi bulunmuyor.")
        return

    print("\nKayıtlı bilgiler:")

    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")

    try:
        choice = int(input("Silmek istediğin bilginin numarasını gir: "))

        if 1 <= choice <= len(notes):
            deleted_note = notes.pop(choice - 1)
            save_memory(memory)
            print(f"Bilgi silindi: {deleted_note}")
        else:
            print("Geçersiz numara girdin.")

    except ValueError:
        print("Lütfen geçerli bir sayı gir.")

def main():
    show_help()

    while True:
        command = input("\nKomut: ").lower().strip()

        if command == "q":
            print("Program sonlandı.")
            break

        elif command == "users":
            show_users()

        elif command == "user":
            show_user()

        elif command == "email":
            show_email()

        elif command == "help":
            show_help()

        elif command == "add":
            add_user()

        elif command == "delete":
            delete_user()

        elif command == "update":
            update_user()

        elif command == "remember":
            remember()

        elif command == "memory":
            show_memory()

        elif command == "forget":
            forget()

        else:
            print("Bilinmeyen komut.")


if __name__ == "__main__":
    main()