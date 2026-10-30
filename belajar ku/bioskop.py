nama = input("nama: ")
tiket = int(input("Jumalah Tiket: "))
total = 0
i = 1

while i <= tiket:
    print("Tiket ke {i}")
    umur = input("Umur: ")
    if umur >= 60:
        print("Kategori Lansia") 
        Harga = 50000
        print("harga", Harga)
    elif umur >= 30:
        print("Kategori Dewasa") 
        Harga = 40000 
        print("harga", Harga)
    elif umur >= 20:
        print("Kategori Remaja") 
        Harga = 30000
        print("harga", Harga)
    elif umur >= 10:
        print("Kategori Anak-Anak") 
        Harga = 20000
        print("harga", Harga)
    elif umur <= 6:
        print("Kategori Balita") 
        Harga = 0
        print("harga", Harga)
    else:
        print("tidak masuk kategori")

    i = i + 1
print("selesai")