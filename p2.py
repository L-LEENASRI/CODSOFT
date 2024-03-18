def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature():
    print("***  Welcome To Temperature Converter  ***\n")
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    choice = int(input("\nEnter your choice (1-7): "))
        
    while(choice != 7):
        temperature = float(input("Enter temperature value: "))
        
        if choice == 1:
            print("Result:", celsius_to_fahrenheit(temperature), "F")
        elif choice == 2:
            print("Result:", fahrenheit_to_celsius(temperature), "C")
        elif choice == 3:
            print("Result:", celsius_to_kelvin(temperature), "K")
        elif choice == 4:
            print("Result:", kelvin_to_celsius(temperature), "C")
        elif choice == 5:
            print("Result:", fahrenheit_to_kelvin(temperature), "K")
        elif choice == 6:
            print("Result:", kelvin_to_fahrenheit(temperature), "F")
        else:
            print("Invalid choice. Please try again.")
            continue
        choice=int(input("\nEnter your choice (1-7): "))
    print("Exiting program...")
        
convert_temperature()
