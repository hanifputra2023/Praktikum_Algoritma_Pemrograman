## Operasi LIST

# Index: 0(-3), 1(-2), 2(-1)
data = ["Ucup", "Adit", "Dudung"]

# Mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

# Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# Manipulasi data list
print(f"data sebelum ditambah = \n{data}")

# Menambahkan item pada list sesuai posisi
# data.insert(posisi, item)
data.insert(1, "Asep")
print(f"data sesudah ditambah = \n{data}")

# Menambah item di akhir list
data.append("Ririn")
print(f"data ditambah lagi = \n{data}")

# Menambahkan list dengan list
data_baru = ["Luffy", "Zoro", "Nami"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# Merubah data index 2 menjadi Jarwo
data[2] = "Jarwo"
print(f"data rubah = \n{data}")

# Menghapus data tertentu
data.remove("Ucup")
print(f"data hapus = \n{data}")

# Menghapus data paling belakang
data.pop()
print(f"data akhir = \n{data}")