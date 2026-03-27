def zadanie1():
    print("--- Zadanie 1: Kalkulator ---")
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    op = input("Wybierz operację (+, -, *, /): ")

    if op == "+": print(f"Wynik: {a + b}")
    elif op == "-": print(f"Wynik: {a - b}")
    elif op == "*": print(f"Wynik: {a * b}")
    elif op == "/": print(f"Wynik: {a / b}" if b != 0 else "Nie dziel przez 0!")

def zadanie2():
    print("--- Zadanie 2: Konwerter Temperatur ---")
    tryb = input("Wybierz C (C->F) lub F (F->C): ").upper()
    temp = float(input("Podaj wartość: "))
    
    if tryb == "C":
        print(f"{temp}°C = {temp * 1.8 + 32}°F")
    elif tryb == "F":
        print(f"{temp}°F = {(temp - 32) / 1.8}°C")

def zadanie3():
    print("--- Zadanie 3: Średnia ocen ---")
    ile = int(input("Ile ocen chcesz podać? "))
    suma = 0
    for i in range(ile):
        ocena = float(input(f"Podaj ocenę {i+1}: "))
        suma += ocena
    
    srednia = suma / ile
    print(f"Średnia: {srednia:.2f}")
    print("Uczeń zdał." if srednia >= 3.0 else "Uczeń nie zdał.")

# MENU GŁÓWNE
while True:
    print("\n--- MENU ZADAŃ ---")
    wybor = input("Wybierz zadanie (1, 2, 3) lub 'q' aby wyjść: ")
    if wybor == "1": zadanie1()
    elif wybor == "2": zadanie2()
    elif wybor == "3": zadanie3()
    elif wybor.lower() == "q": break
    else: print("Błędny wybór!")