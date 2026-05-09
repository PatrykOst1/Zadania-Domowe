using System;

namespace VetClinic {
    // 1. ABSTRAKCJA
    public abstract class Animal {
        public int Id { get; set; }
        public string? Name { get; set; }
        public int Age { get; set; }
        public string? OwnerName { get; set; }
        
        // Polimorfizm - każde zwierzę zareaguje inaczej
        public abstract void MakeSound();
    }

    // 2. DZIEDZICZENIE
    public class Dog : Animal {
        public string? Breed { get; set; }
        public override void MakeSound() => Console.WriteLine($"{Name} szczeka: Hau! Hau!");
    }

    public class Cat : Animal {
        public bool IsIndoor { get; set; }
        public override void MakeSound() => Console.WriteLine($"{Name} miauczy: Miau!");
    }

    public class Parrot : Animal {
        public double WingSpan { get; set; }
        public override void MakeSound() => Console.WriteLine($"{Name} skrzeczy: Kraa!");
    }

    // 3. ENKAPSULACJA (Ochrona danych)
    public class Vet {
        private double _salary;
        private string? _specialization;

        public void SetSpecialization(string spec) => _specialization = spec;
        public string? GetSpecialization() => _specialization;

        public void PerformCheckup(Animal animal) {
            Console.WriteLine($"\n[Badanie] Lekarz bada pacjenta...");
            animal.MakeSound(); // Polimorfizm w praktyce
        }

        // PRZECIĄŻANIE METOD (Dwie metody o tej samej nazwie, ale innych parametrach)
        public void PrescribeMeds(string medicineName) {
            Console.WriteLine($"[Recepta] Przepisano: {medicineName} (Standardowa dawka)");
        }
        
        public void PrescribeMeds(string medicineName, string dosage) {
            Console.WriteLine($"[Recepta] Przepisano: {medicineName}, Dawkowanie: {dosage}");
        }
    }

    // 4. KOMPOZYCJA
    public class Visit {
        public Vet Doctor { get; set; }
        public Animal Patient { get; set; }
        public DateTime Date { get; set; }
        public string? Diagnosis { get; set; }

        public Visit(Vet vet, Animal animal) {
            Doctor = vet;
            Patient = animal;
            Date = DateTime.Now;
        }
    }

    // 5. METODY I WŁAŚCIWOŚCI STATYCZNE
    public static class ClinicManager {
        public static int GlobalVisitCounter = 0;

        public static void ScheduleVisit(Vet vet, Animal animal) {
            GlobalVisitCounter++;
            Visit newVisit = new Visit(vet, animal);
            Console.WriteLine($"\n=> ZAPISANO WIZYTĘ. Łączna liczba wizyt w klinice: {GlobalVisitCounter}");
        }
    }

    // INTERAKTYWNE MENU KONSOLOWE
    class Program {
        static void Main(string[] args) {
            Vet lekarz = new Vet();
            lekarz.SetSpecialization("Chirurg");

            while (true) {
                Console.WriteLine("\n--- KLINIKA WETERYNARYJNA ---");
                Console.WriteLine("1. Zarejestruj Psa");
                Console.WriteLine("2. Zarejestruj Kota");
                Console.WriteLine("3. Zarejestruj Papugę");
                Console.WriteLine("4. Zakończ program");
                Console.Write("Wybierz opcję: ");
                
                string? wybor = Console.ReadLine();
                if (wybor == "4") break;

                Console.Write("Podaj imię zwierzaka: ");
                string imie = Console.ReadLine() ?? "Nieznane";

                Animal? pacjent = null;

                switch (wybor) {
                    case "1": pacjent = new Dog { Name = imie, Breed = "Mieszaniec" }; break;
                    case "2": pacjent = new Cat { Name = imie, IsIndoor = true }; break;
                    case "3": pacjent = new Parrot { Name = imie, WingSpan = 20.5 }; break;
                    default: 
                        Console.WriteLine("Błędny wybór. Spróbuj ponownie."); 
                        continue;
                }

                // Logika systemu kliniki
                ClinicManager.ScheduleVisit(lekarz, pacjent);
                lekarz.PerformCheckup(pacjent);
                
                Console.Write("Czy chcesz podać dokładną dawkę leku? (T/N): ");
                if (Console.ReadLine()?.ToUpper() == "T") {
                    lekarz.PrescribeMeds("Antybiotyk", "2 razy dziennie po pół tabletki"); // Przeciążenie 2
                } else {
                    lekarz.PrescribeMeds("Witaminy"); // Przeciążenie 1
                }
            }
        }
    }
}