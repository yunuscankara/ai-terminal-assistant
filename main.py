#def calculate_average(*args:int)-> float:
 #   return sum(args)/len(args)

#print(calculate_average(10, 20))
#print(calculate_average(5, 10, 15, 20))
#print(calculate_average(1, 2, 3, 4, 5))

#def calculate_discount(price, discount=10):
 #   discount_amount = price * discount / 100
  #  return price - discount_amount
#print(calculate_discount(100))
#print(calculate_discount(200, 20))

""" def show_user(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_user(
    name="Yunus",
    age=23,
    city="Istanbul",
    job="AI Developer"
)


name = "Yunus"

def show_name():
    name = "Mark"
    print(name)

show_name()
print(name)

try:
    number = int(input("Bir sayı girin: "))
    print(number * 2)
except:
    print("Lütfen bir sayı girin")
"""  
## AI TERMİNAL ASSİSTANT

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
 