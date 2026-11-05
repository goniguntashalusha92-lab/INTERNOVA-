# Task 3c: Temperature conversion for a weather AI
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(f"{celsius} C = {fahrenheit:.2f} F = {kelvin:.2f} K")

if celsius >= 35:
    print("Weather AI: It is very hot. Stay hydrated!")
elif celsius >= 20:
    print("Weather AI: Pleasant weather.")
elif celsius >= 10:
    print("Weather AI: It is cool. Carry a light jacket.")
else:
    print("Weather AI: It is cold. Wear warm clothes.")
