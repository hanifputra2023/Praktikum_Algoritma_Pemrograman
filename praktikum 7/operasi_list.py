## Operasi LIST

# Index: 0(-3), 1(-2), 2(-1)
data_angka = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 8, 9, 0]
print(f"data angka = \n{data_angka}")

# Count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# Mengambil posisi data
data = ["Rendi", "Iqbal", "Gana", "Khairil"]
print(f"data = {data}")

index_iqbal = data.index("Iqbal")
index_gana = data.index("Gana")
print(f"index si Iqbal = {index_iqbal}")
print(f"index si Gana = {index_gana}")

# Mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data sebelum sort = {data}")
data.sort()
print(f"data sort = {data}")

# Membalik urutan list
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka}")
print(f"data di reverse = \n{data}")