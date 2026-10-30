kendaraan = ["motor", "mobil", "sepeda", "bus"]
kendaraan.append("truk")
print(kendaraan)

kendaraan.insert(1, "becak")
print(kendaraan)

kendaraan.pop()
print(kendaraan)

kendaraan[2] = "kereta"
print(kendaraan)

jumlah_kendaraan = len(kendaraan)
print(f"Jumlah kendaraan: {jumlah_kendaraan}")
