using System;

class Program {
    static void Main() {
        while (true) {
            Console.WriteLine("\nWybierz zadanie (1, 2, 3) lub 'q' aby wyjść:");
            string wybor = Console.ReadLine();

            if (wybor == "1") Zadanie1();
            else if (wybor == "2") Zadanie2();
            else if (wybor == "3") Zadanie3();
            else if (wybor.ToLower() == "q") break;
            else Console.WriteLine("Błędny wybór!");
        }
    }

    static void Zadanie1() {
        Console.WriteLine("--- Kalkulator ---");
        Console.Write("Liczba 1: "); double a = double.Parse(Console.ReadLine());
        Console.Write("Liczba 2: "); double b = double.Parse(Console.ReadLine());
        Console.Write("Znak (+,-,*,/): "); string op = Console.ReadLine();
        if (op == "+") Console.WriteLine($"Wynik: {a+b}");
        else if (op == "/") Console.WriteLine(b != 0 ? $"Wynik: {a/b}" : "Błąd!");
        // ... (analogicznie - i * )
    }

    static void Zadanie2() {
        Console.WriteLine("--- Temperatura ---");
        Console.Write("Wybierz C lub F: "); string t = Console.ReadLine().ToUpper();
        Console.Write("Wartość: "); double v = double.Parse(Console.ReadLine());
        if (t == "C") Console.WriteLine($"{v}°C = {v * 1.8 + 32}°F");
        else if (t == "F") Console.WriteLine($"{v}°F = {(v - 32) / 1.8}°C");
    }

    static void Zadanie3() {
        Console.WriteLine("--- Średnia ---");
        Console.Write("Ile ocen? "); int ile = int.Parse(Console.ReadLine());
        double suma = 0;
        for (int i = 0; i < ile; i++) {
            Console.Write($"Ocena {i+1}: ");
            suma += double.Parse(Console.ReadLine());
        }
        double srednia = suma / ile;
        Console.WriteLine($"Średnia: {srednia:F2}. " + (srednia >= 3.0 ? "Zdał" : "Nie zdał"));
    }
}
