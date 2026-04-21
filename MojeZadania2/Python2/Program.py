class Reading:
    def __init__(self, value, unit="C"):
        self.value = value
        self.unit = unit

class Alert:
    def __init__(self, limit):
        self.limit = limit

    def check(self, reading):
        if reading.value > self.limit:
            print(f"OSTRZEŻENIE: Temperatura {reading.value}{reading.unit} przekroczyła limit!")

class Sensor:
    def __init__(self, name):
        self.name = name
        self.history = []

    def get_reading(self, val):
        r = Reading(val)
        self.history.append(r)
        return r

# Użycie:
sensor = Sensor("Termometr pokojowy")
alarm = Alert(30)

# Symulacja odczytu
wynik = sensor.get_reading(32)
alarm.check(wynik)