def calculate(a, b, operation):

    if operation == "sum":

        return a + b

    elif operation == "subtract":

        return a - b

    elif operation == "multiply":

        return a * b

    elif operation == "divide":

        return a / b

    else:

        return "Geçerli bir işlem girin"

def main():

    print("=== AI Terminal Assistant ===")

    print("Kullanabileceğiniz işlemler:")

    print("sum")

    print("subtract")

    print("multiply")

    print("divide")

    print("q - Çıkış")

    while True:

        operation = input("İşlem seçin: ")

        if operation == "q":

            break

        try:

            a = int(input("Bir sayı girin: "))

            b = int(input("Bir sayı girin: "))

            result = calculate(a, b, operation)

            print("Sonuç:", result)

        except ValueError:

            print("Lütfen geçerli bir sayı girin.")

        except ZeroDivisionError:

            print("Bir sayı 0'a bölünemez.")

    print("Program Sonlandı")

if __name__ == "__main__":

    main()    
 