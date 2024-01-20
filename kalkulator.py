def dodaj(x, y):
    return x + y

def odejmij(x, y):
    return x - y

def pomnoz(x, y):
    return x * y

def podziel(x, y):
    if y == 0:
        return "Błąd: Dzielenie przez zero!"
    return x / y

while True:
    print("Operacje:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")

    wybor = input("Wybierz operację (1/2/3/4/5): ")

    if wybor in ('1', '2', '3', '4'):
        num1 = float(input("Wprowadź pierwszą liczbę: "))
        num2 = float(input("Wprowadź drugą liczbę: "))

        if wybor == '1':
            print("Wynik: ", dodaj(num1, num2))

        elif wybor == '2':
            print("Wynik: ", odejmij(num1, num2))

        elif wybor == '3':
            print("Wynik: ", pomnoz(num1, num2))

        elif wybor == '4':
            print("Wynik: ", podziel(num1, num2))

    elif wybor == '5':
        break
    else:
        print("Nieprawidłowy wybór")

