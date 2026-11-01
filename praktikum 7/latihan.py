# List awal
kendaraan = ["motor", "mobil", "sepeda", "bus"]

# a. Tambahkan 'truk' di akhir list
kendaraan.append("truk")
print(f"a. Tambah 'truk' di akhir = {kendaraan}")

# b. Sisipkan 'becak' pada index ke-1
kendaraan.insert(1, "becak")
print(f"b. Sisip 'becak' di index 1 = {kendaraan}")

# c. Hapus data yang berada paling belakang dari list tersebut
kendaraan.pop()
print(f"c. Hapus data paling belakang = {kendaraan}")

# d. Ubah elemen 'sepeda' menjadi 'skuter'
# Karena posisi 'sepeda' ada di indeks ke-3, kita ubah langsung:
kendaraan[3] = "skuter"
print(f"d. Ubah 'sepeda' jadi 'skuter' = {kendaraan}")

# e. Tampilkan informasi jumlah total data di dalam list tersebut
jumlah_kendaraan = len(kendaraan)
print(f"e. Jumlah total data = {jumlah_kendaraan}")