from abc import ABC, abstractmethod
from datetime import datetime

# 1. ABSTRAKCJA
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

# 2. DZIEDZICZENIE I POLIMORFIZM
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} szczeka: Hau! Hau!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} miauczy: Miau!")

class Parrot(Animal):
    def make_sound(self):
        print(f"{self.name} skrzeczy: Kraa!")

# 3. ENKAPSULACJA I "PRZECIĄŻANIE" (symulowane)
class Vet:
    def __init__(self, specialization):
        self.__specialization = specialization # Pole prywatne

    def perform_checkup(self, animal):
        print("\n[Badanie] Lekarz bada pacjenta...")
        animal.make_sound()

    def prescribe_meds(self, medicine_name, dosage=None):
        if dosage:
            print(f"[Recepta] Przepisano: {medicine_name}, Dawkowanie: {dosage}")
        else:
            print(f"[Recepta] Przepisano: {medicine_name} (Standardowa dawka)")

# 4. KOMPOZYCJA
class Visit:
    def __init__(self, vet, animal):
        self.vet = vet
        self.animal = animal
        self.date = datetime.now()

# 5. METODY I POLA STATYCZNE
class ClinicManager:
    global_visit_counter = 0

    @staticmethod
    def schedule_visit(vet, animal):
        ClinicManager.global_visit_counter += 1
        Visit(vet, animal)
        print(f"\n=> ZAPISANO WIZYTĘ. Łączna liczba wizyt: {ClinicManager.global_visit_counter}")

# --- INTERAKTYWNE MENU KONSOLOWE ---
if __name__ == "__main__":
    lekarz = Vet("Chirurg")

    while True:
        print("\n--- KLINIKA WETERYNARYJNA ---")
        print("1. Pies | 2. Kot | 3. Papuga | 4. Zakończ")
        wybor = input("Wybierz opcję: ")
        
        if wybor == "4":
            break
            
        if wybor not in ["1", "2", "3"]:
            print("Błędny wybór!")
            continue

        imie = input("Podaj imię zwierzaka: ")

        if wybor == "1": pacjent = Dog(imie)
        elif wybor == "2": pacjent = Cat(imie)
        elif wybor == "3": pacjent = Parrot(imie)

        ClinicManager.schedule_visit(lekarz, pacjent)
        lekarz.perform_checkup(pacjent)
        
        odp = input("Czy chcesz podać dokładną dawkę leku? (T/N): ").strip().upper()
        if odp == "T":
            lekarz.prescribe_meds("Antybiotyk", "2 razy dziennie po pół tabletki")
        else:
            lekarz.prescribe_meds("Witaminy")