panjang = int(input("Masukkan Panjang Ruangan: "))
lebar = int(input("Masukkan Lebar Ruangan: "))
tinggi = int(input("Masukkan Tinggi Ruangan: "))

Luas_alas = panjang * lebar
Volume = panjang * lebar * tinggi
Keliling_rusuk = 4 * (panjang + lebar + tinggi)
jumlah_karpet = Luas_alas // 3
sisa_luas = Luas_alas % 3

Luas = Luas_alas > 50
volume_akhir = Volume == 480

print(Luas_alas)
print(Volume)
print(Keliling_rusuk)
print(jumlah_karpet)
print(sisa_luas)
print(Luas)
print(volume_akhir)