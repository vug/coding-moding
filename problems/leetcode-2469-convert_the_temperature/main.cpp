#include <vector>
#include "../include/fmt/core.h"

std::vector<double> convertTemperature(double celsius)
{
    return {celsius + 273.15, celsius * 1.80 + 32.00};
}

class Temperature {
    double celcius{};
    double kelvin{};
    double fahrenheit{};

    Temperature() = default;
    Temperature(double c, double k, double f)
        : celcius(c), kelvin(k), fahrenheit(f) { }
    
public:
    double getCelcius() const { return celcius; }
    double getKelvin() const { return kelvin; }
    double getFahrenheit() const { return fahrenheit; }

    Temperature& setCelcius(double c) {
        celcius = c;
        kelvin = c + 273.15;
        fahrenheit = c * 1.80 + 32.00;
        return *this;
    }

    // Temperature& setKelvin(double k) { ... }

    static Temperature makeFromCelcius(double celcius) {
        Temperature t;
        return t.setCelcius(celcius);
    }

    // Temperature makeFromKelvin(double kelvin) { ... }
};

int main() {
    const double c = 36.50;
    std::vector<double> result = convertTemperature(c);
    fmt::print("celcius {}, kelvin {}, fahrenheit {}\n", c, result[0], result[1]);

    Temperature t = Temperature::makeFromCelcius(c);
    fmt::print("celcius {}, kelvin {}, fahrenheit {}\n", t.getCelcius(), t.getKelvin(), t.getFahrenheit());
}