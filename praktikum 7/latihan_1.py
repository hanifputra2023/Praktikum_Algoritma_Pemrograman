angka = [75, 80, 90, 75, 85, 100, 65] 
indeks_angka = angka.index(100)
print(f"indeks angka 100 = {indeks_angka}")

nilai_siswa = angka.count(75)
print(f"jumlah siswa yang mendapat nilai 75 = {nilai_siswa}")

list_skor_terkecil = sorted(angka)
print(f"list skor terkecil = {list_skor_terkecil}")

list_skor_terbesar = sorted(angka, reverse=True)
print(f"list skor terbesar = {list_skor_terbesar}")