def convert_temperature(value, unit):
    if unit == "C":
        return (value * 9/5) + 32  
    elif unit == "F":
        return (value - 32) * 5/9  
    else:
        return None


temp = float(input("Enter temperature: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()


result = convert_temperature(temp, unit)


if result is not None:
    if unit == "C":
        print("Temperature in Fahrenheit:", result)
    else:
        print("Temperature in Celsius:", result)
else:
    print("Invalid unit entered!")