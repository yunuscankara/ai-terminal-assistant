import requests
import json



API_URL = "https://jsonplaceholder.typicode.com/users"


def get_users():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        users = response.json()

        if not isinstance(users, list):
            print("API beklenmeyen bir yanıt döndürdü.")
            return []

        return users

    except requests.exceptions.RequestException as error:
        print(f"API bağlantı hatası: {error}")
        return []

    except ValueError as error:
        print(f"API yanıtı okunamadı: {error}")
        return []


def find_user(users, user_id):
    for user in users:
        if user.get("id") == user_id:
            return user

    return None


def show_email():
    users = get_users()

    if not users:
        print("Kullanıcı bilgileri alınamadı.")
        return

    try:
        user_id = int(input("Kullanıcı ID: "))
    except ValueError:
        print("ID sadece sayı olmalıdır.")
        return

    user = find_user(users, user_id)

    if user:
        print("Email:", user.get("email", "E-posta bulunamadı."))
    else:
        print("Kullanıcı bulunamadı.")


def show_users():
    users = get_users()

    if not users:
        print("Gösterilecek kullanıcı bulunamadı.")
        return

    for user in users:
        print(user.get("name", "İsimsiz kullanıcı"))


def show_user():
    users = get_users()

    if not users:
        print("Kullanıcı bilgileri alınamadı.")
        return

    try:
        user_id = int(input("Kullanıcı ID: "))
    except ValueError:
        print("ID sadece sayı olmalıdır.")
        return

    user = find_user(users, user_id)

    if user:
        print("İsim:", user.get("name", "Bilinmiyor"))
        print("Email:", user.get("email", "Bilinmiyor"))
        print("Telefon:", user.get("phone", "Bilinmiyor"))

        address = user.get("address") or {}
        print("Şehir:", address.get("city", "Bilinmiyor"))
    else:
        print("Kullanıcı bulunamadı.")


def show_help():
    print("\n=== AI Terminal Assistant ===")
    print("users    - Kullanıcıları getir")
    print("user     - Kullanıcı bilgisi getir")
    print("email    - Kullanıcı e-postasını getir")
    print("add      - Yeni kullanıcı ekleme isteği gönder")
    print("delete   - Kullanıcı silme isteği gönder")
    print("update   - Kullanıcı güncelleme isteği gönder")
    print("remember - Hafızaya bilgi kaydet")
    print("memory   - Kayıtlı bilgileri göster")
    print("forget   - Hafızadan bilgi sil")
    print("chat     - Yerel yapay zekâ ile sohbet et")
    print("help     - Komutları göster")
    print("q        - Programdan çık")


def add_user():
    name = input("İsim: ").strip()

    if not name:
        print("İsim boş bırakılamaz.")
        return

    try:
        age = int(input("Yaş: "))

        if age <= 0:
            print("Yaş sıfırdan büyük olmalıdır.")
            return

    except ValueError:
        print("Yaş sadece sayı olmalıdır.")
        return

    job = input("Meslek: ").strip()

    user = {
        "name": name,
        "age": age,
        "job": job
    }

    try:
        response = requests.post(
            API_URL,
            json=user,
            timeout=10
        )
        response.raise_for_status()

        print("Kullanıcı ekleme isteği başarılı.")
        print(response.json())

    except requests.exceptions.RequestException as error:
        print(f"Kullanıcı eklenemedi: {error}")

    except ValueError as error:
        print(f"Sunucu yanıtı okunamadı: {error}")


def delete_user():
    try:
        user_id = int(input("Kullanıcı ID: "))

        if user_id <= 0:
            print("ID pozitif bir sayı olmalıdır.")
            return

    except ValueError:
        print("ID sadece sayı olmalıdır.")
        return

    try:
        response = requests.delete(
            f"{API_URL}/{user_id}",
            timeout=10
        )
        response.raise_for_status()

        print("Silme isteği başarılı.")

    except requests.exceptions.RequestException as error:
        print(f"Kullanıcı silinemedi: {error}")


def update_user():
    try:
        user_id = int(input("Kullanıcı ID: "))

        if user_id <= 0:
            print("ID pozitif bir sayı olmalıdır.")
            return

    except ValueError:
        print("ID sadece sayı olmalıdır.")
        return

    users = get_users()

    if not users:
        print("Kullanıcı listesi alınamadı.")
        return

    user = find_user(users, user_id)

    if not user:
        print("Kullanıcı bulunamadı.")
        return

    name = input("Yeni isim: ").strip()

    if not name:
        print("İsim boş bırakılamaz.")
        return

    try:
        age = int(input("Yaş: "))

        if age <= 0:
            print("Yaş sıfırdan büyük olmalıdır.")
            return

    except ValueError:
        print("Yaş sadece sayı olmalıdır.")
        return

    job = input("Meslek: ").strip()

    updated_user = {
        "name": name,
        "age": age,
        "job": job
    }

    try:
        response = requests.put(
            f"{API_URL}/{user_id}",
            json=updated_user,
            timeout=10
        )
        response.raise_for_status()

        print("Güncelleme isteği başarılı.")
        print(response.json())

    except requests.exceptions.RequestException as error:
        print(f"Kullanıcı güncellenemedi: {error}")

    except ValueError as error:
        print(f"Sunucu yanıtı okunamadı: {error}")




MEMORY_FILE = "memory.json"


def load_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            memory = json.load(file)

        if not isinstance(memory, dict):
            print("Hafıza dosyasının formatı geçersiz.")
            print("Mevcut dosya korunuyor.")
            return None

        notes = memory.get("notes")

        if not isinstance(notes, list):
            print("Hafıza dosyasında notes listesi bulunamadı.")
            print("Mevcut dosya korunuyor.")
            return None

        if not all(isinstance(note, str) for note in notes):
            print("Hafıza dosyasında geçersiz notlar var.")
            print("Mevcut dosya korunuyor.")
            return None

        return memory

    except FileNotFoundError:
        print("Hafıza dosyası bulunamadı. Yeni hafıza oluşturuluyor.")

        memory = {"notes": []}

        if save_memory(memory):
            return memory

        print("Hafıza dosyası oluşturulamadı.")
        return None

    except json.JSONDecodeError as error:
        print(f"Hafıza dosyası bozuk veya geçersiz JSON içeriyor: {error}")
        print("Mevcut dosya korunuyor.")
        return None

    except OSError as error:
        print(f"Hafıza dosyasına erişilemedi: {error}")
        return None


def save_memory(memory):
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump(
                memory,
                file,
                ensure_ascii=False,
                indent=4
            )

        return True

    except (OSError, TypeError, ValueError) as error:
        print(f"Hafıza kaydedilirken hata oluştu: {error}")
        return False


def remember():
    memory = load_memory()

    if memory is None:
        print("Hafıza yüklenemedi. Bilgi kaydedilemedi.")
        return

    note = input("Hatırlanacak bilgi: ").strip()

    if not note:
        print("Boş bilgi kaydedilemez.")
        return

    memory["notes"].append(note)

    if save_memory(memory):
        print("Bilgi başarıyla kaydedildi.")
    else:
        print("Bilgi kaydedilemedi.")


def show_memory():
    memory = load_memory()

    if memory is None:
        print("Hafıza görüntülenemedi.")
        return

    notes = memory["notes"]

    if not notes:
        print("Henüz kayıtlı bilgi yok.")
        return

    print("\nKayıtlı bilgiler:")

    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")


def forget():
    memory = load_memory()

    if memory is None:
        print("Hafıza yüklenemedi. Silme işlemi yapılamadı.")
        return

    notes = memory["notes"]

    if not notes:
        print("Silinecek bir bilgi bulunmuyor.")
        return

    print("\nKayıtlı bilgiler:")

    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")

    try:
        choice = int(input("Silmek istediğin bilginin numarasını gir: "))

    except ValueError:
        print("Lütfen geçerli bir sayı gir.")
        return

    if not 1 <= choice <= len(notes):
        print("Geçersiz numara girdin.")
        return

    # Silmeden önce mevcut listeyi koru.
    deleted_note = notes.pop(choice - 1)

    if save_memory(memory):
        print(f"Bilgi silindi: {deleted_note}")
    else:
        # Kaydetme başarısız olursa mevcut süreçteki listeyi geri yükle.
        notes.insert(choice - 1, deleted_note)
        print("Silme işlemi kaydedilemedi. Bilgi geri yüklendi.")


conversation_history = []

SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "Sen yardımcı bir yapay zekâ asistanısın. "
        "Her zaman Türkçe cevap ver. "
        "Kullanıcı başka bir dilde yazsa bile Türkçe cevap ver. "
        "Cevaplarını açık, anlaşılır ve doğal bir Türkçeyle oluştur."
    )
}


def chat():
    print("AI sohbetine hoş geldin! Çıkmak için 'q' yaz.")

    while True:
        user_message = input("\nSen: ").strip()

        if user_message.lower() == "q":
            print("Sohbet sonlandırıldı.")
            break

        if not user_message:
            print("Lütfen boş mesaj göndermeyin.")
            continue

        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        try:
            response = requests.post(
                "http://localhost:11434/api/chat",
                json={
                    "model": "qwen2.5:3b",
                    "messages": [
                        SYSTEM_MESSAGE,
                        *conversation_history
                    ],
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()
            data = response.json()

            message = data.get("message")

            if not isinstance(message, dict):
                raise ValueError("Ollama beklenen yanıt formatını döndürmedi.")

            answer = message.get("content")

            if not isinstance(answer, str):
                raise ValueError("Yapay zekâ yanıtı geçersiz.")

            conversation_history.append({
                "role": "assistant",
                "content": answer
            })

            print(f"AI: {answer}")

        except requests.exceptions.RequestException as error:
            print(f"Ollama bağlantı hatası: {error}")
            conversation_history.pop()

        except (ValueError, KeyError) as error:
            print(f"Yapay zekâ yanıtı işlenemedi: {error}")
            conversation_history.pop()



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

        elif command == "chat":
            chat()

        else:
            print("Bilinmeyen komut. Komutları görmek için 'help' yaz.")


if __name__ == "__main__":
    main()