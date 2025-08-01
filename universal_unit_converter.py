def convert_length(value, from_unit, to_unit):

    units = {
        "meter" : 1,
        "kilometer" : 1000,
        "centimeter" : 0.01,
        "milimeter" : 0.001,
        "mile" : 1609.34,
        "yard" : 0.9144,
        "foot" : 0.3048,
        "inch" : 0.0254
    }

    return value * units[from_unit] / units[to_unit]

def convert_weight(value, from_unit, to_unit):
    
    units = {
        "kilogram" : 1,
        "gram" : 0.001,
        "miligram" : 0.000001,
        "pound" : 0.453592,
        "ounce" :0.0283495
    }

    return value * units[from_unit] / units[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
       return value
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return(value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
        elif from_unit == "fahrenheit":
            if to_unit == "celcius":
                return(value - 32) * 5/9
            elif to_unit == "kelvin":
                return(value - 32) * 5/9 + 273.15
            elif from_unit == "kelvin":
                 if to_unit == "celsius":
                    return value - 273.15
            elif to_unit == "fahrenheit":
                return(value - 273.15) * 9/5 + 32
    

def convert_time(value, from_unit, to_unit):
    units = {
        "second" : 1,
        "minute" : 60,
        "hour" : 3600,
        "day" : 86400
    }
    return value * units[from_unit] / units[to_unit]


def main():
    converters = {
        "length" : convert_length,
        "weight" : convert_weight,
        "temperature" : convert_temperature,
        "time" : convert_time
    }

    while True:
        print("\n--- Unit Converter ---")
        print("Categories:", ', '.join(converters.keys()))
        category = input("Choose category (or 'exit'): ").lower()
        if category == 'exit':
            break


        if category not in converters:
            print("Invalid category. Try again.")
            continue


        from_unit = input("From unit: ").lower()
        to_unit = input("To unit: ").lower()
        value = float(input("Value to convert: "))



        try:
            result = converters[category](value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result} {to_unit}")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()




