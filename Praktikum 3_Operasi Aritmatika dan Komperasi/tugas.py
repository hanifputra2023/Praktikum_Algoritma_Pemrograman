Panjang = int(input("Masukkan panjang: "))
Lebar = int(input("Masukkan lebar: "))
Tinggi = int(input("Masukkan tinggi: "))

print("================================")
Volume = Panjang * Lebar * Tinggi
print("Volume balok adalah: ", Volume)

Keliling = 2 * (Panjang + Lebar + Tinggi)
print("Keliling balok adalah: ", Keliling)

Luas = Panjang * Lebar
print("Luas balok adalah: ", Luas)
print("================================")
print("Maka Volume", Volume, "Keliling", Keliling, "dan Luas", Luas)
print("================================")
luas_bangunan = Luas > 50
print("Apakah luas bangunan lebih dari 50?", luas_bangunan)
print("================================")
volume_bangunan = Volume == 480
print("Apakah volume bangunan sama dengan 480?", volume_bangunan)