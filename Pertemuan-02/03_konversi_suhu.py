
# Latihan 3 Konversi Suhu

KELVIN_OFFSET = 273.15

celsius = float(input("Masukkan suhu Celsius: "))

fahrenheit = (9/5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

print("\n===== HASIL KONVERSI =====")
print(f"Celsius    : {celsius:.2f} °C")
print(f"Fahrenheit : {fahrenheit:.2f} °F")
print(f"Kelvin     : {kelvin:.2f} K")