Panjang = int(input("Masukkan panjang: "))
Lebar = int(input("Masukkan lebar: "))
Tinggi = int(input("Masukkan tinggi: "))

print("================================")
Volume = Panjang * Lebar * Tinggi
print("Volume balok adalah: ", Volume)

Keliling = 4 * (Panjang + Lebar + Tinggi)
print("Keliling balok adalah: ", Keliling)

Luas_bangunan = 2 * (Panjang * Lebar) + 2 * (Panjang * Tinggi) + 2 * (Lebar * Tinggi)
print("Luas balok adalah: ", Luas_bangunan)
print("================================")
print("Maka Volume", Volume, "Keliling", Keliling, "dan Luas", Luas_bangunan)
print("================================")
luas_bangunan = Luas_bangunan > 50
print("Apakah luas bangunan lebih dari 50?", luas_bangunan)
print("================================")
volume_bangunan = Volume == 480
print("Apakah volume bangunan sama dengan 480?", volume_bangunan)