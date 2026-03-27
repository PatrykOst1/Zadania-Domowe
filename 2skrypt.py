import math

while True:
    try:
        a, b, c = map(float, input("Podaj a b c: ").split())
        break
    except ValueError:
        print("Podaj DOKŁADNIE trzy liczby oddzielone spacją, np. 1 5 6.")

if a == 0:
    print("brak")
else:
    d = b*b - 4*a*c
    if d < 0:
        print("brak")
    elif d == 0:
        print(-b / (2*a))
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(x1, x2)
