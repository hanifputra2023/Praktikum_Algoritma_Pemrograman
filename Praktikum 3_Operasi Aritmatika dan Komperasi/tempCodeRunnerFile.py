
#program konversi calcius ke satuan lain
print("\nProgram Konversi Satuan Temperature")
celcius = float(input("Masukkan suhu dalam Celcius: "))
print("Suhu adalah", celcius, "Celcius")

#reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah", reamur, "Reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")

#kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah", kelvin, "Kelvin")