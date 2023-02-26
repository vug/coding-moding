# Conversions, units, serving data

https://leetcode.com/problems/convert-the-temperature/

## Braket initialization

This problem is too simple to analyze in terms of logic.

I used braket initialization and return type deduction to have shorter, cleaner code

```cpp
std::vector<double> convertTemperature(double celsius) {
    return {celsius + 273.15, celsius * 1.80 + 32.00};
}
```

But I remember, using braketed list for vector initialization when there are only two arguments was not safe or something.

## Data structures

I think storing different units in the same vector is not a good idea. Users need to remember the indices corresponding to unit. Which can be done by `const int KELVIN_INDEX = 1;` etc. but why? Vector is overkill, and also not fit.

Instead
* Use a struct to store multiple units
* Have a physical quantity type that support multiple units. Ex: temperature type, with units given as template parameters, similar to chrono's duration that can be read as seconds or milliseconds etc.

```cpp
struct Temperature {
    double celcius;
    double kelvin;
    double fahrenheit;

    Temperature(double celcius) : celcius(celcius) {
        kelvin = celsius + 273.15;
        fahrenheit = celsius * 1.80 + 32.00;
    };
};
```

The problem with above is the constructor cannot be overloaded for different units. So, we need factory methods.

```cpp
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
```

* Note that default constructor initializes all units with 0, which is not a valid state. Therefore we didn't make it public. 
* However, for code reuse purposes, instead of `return {celcius, celcius + 273.15, celcius * 1.80 + 32.00;}` we reused `setCelcius` in `makeFromCelcius()`.
* This requires conversion from and to any two units. However, we can pick a canonical unit, and for ever other unit, we first convert to canonical one and then to other one
* Still, I'll prefer a `Temperature<Celcius>` templated type.

## Generalizations

* Both ways conversions from any two units, not only from Celcius to other two
* More units
    * To make extension easier, we might choose to have a canonical unit
* If we don't need to calculate all units per temperature, we might not need to cache all of them.
  * just do the conversion on-the-fly (not at construction).
  * If same unit might be asked multiple times, then memoize.
* Temperature type with multiple units
* Serving this from back-end
  * maybe carrying every unit over network is not a good idea