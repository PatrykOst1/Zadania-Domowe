using System;
using System.Collections.Generic;

public class Reading {
    public double Value { get; set; }
    public Reading(double val) { Value = val; }
}

public class Alert {
    public double Limit { get; set; }
    public Alert(double lim) { Limit = lim; }

    public void Check(Reading r) {
        if (r.Value > Limit) {
            Console.WriteLine($"ALARM: {r.Value}C przekracza limit!");
        }
    }
}

public class Sensor {
    public List<Reading> History = new List<Reading>();

    public Reading TakeMeasurement(double val) {
        Reading r = new Reading(val);
        History.Add(r);
        return r;
    }
}

class Program {
    static void Main() {
        Sensor s = new Sensor();
        Alert a = new Alert(25.0);

        Reading m = s.TakeMeasurement(28.5);
        a.Check(m);
    }
}