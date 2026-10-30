batas = 3
total = 0

while total < batas:
    nama = input("Nama Mahasiswa: ")
    nilai = float(input("Nilai Mahasiswa: "))
    if nilai >= 85:
        print(f"{nama} nilai {nilai} Kategori Sangat Baik")
    
    elif nilai >= 80:
        print(f"{nama} nilai {nilai} Kategori Baik")

    elif nilai >= 75:
        print(f"{nama} nilai {nilai} Kategori kurang")

    elif nilai >= 50:
        print(f"{nama} nilai {nilai} Kategori kurang")

    elif nilai >= 10:
        print(f"{nama} nilai {nilai} Kategori sangat kurang")
    
    else:
        print(f"{nama} nilai {nilai} Kategori tidak masuk ")
    total = total + 1


print("selesai")

