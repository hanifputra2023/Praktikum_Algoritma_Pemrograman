#perulangan (loop) for

angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)

# for kondisi:
# aksi

#dengan list
angka2 = [0, 1, 2, 3, 4, 5] # ini adalah list
print(angka2)

for i in angka2:
    print(f"i sekarang adalah {i}") #print(f) adalah kombinasi text dan variabel
print("akhri dari perulangan")

for i in angka2:
    print("i sekarang adalah" ,i ) #bisa juga tanpa menggunakan (f) tetapi untuk variable i di taruh luar dari text
print("akhri dari perulangan")

# dengan range
angka3 = range(10) # ini adalah range

for i in angka3:
    print(f"i sekarang adalah {i}")
print("akhir dari perulangan\n")

angka4 = range(1, 11) # ini adalah range dari 1 sampai 10
for i in angka4:
    print(f"i sekarang adalah {i}")
print("akhir dari perulangan\n")

# menggunakan string
data_string = "nanda"
for huruf in data_string:
    print(huruf)
print("akhir dari perulangan\n")

