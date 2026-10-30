# #pengelola wahana ingin permainan otomatis
# 1. memeriksa kelayakan pengunjuk naik wahana ekstrem (roller coster)
# 2. menentukan kategori harga tiket menggunakan kombinasi 
# variabel umur, tinggi badan, dan status keanggotaan (member)
for test in range(1, 10):
    nama = input("Masukkan Nama: ")
    umur = int(input("Masukkan Umur: "))
    tinggi_badan = float(input("Masukkan Tinggi Badan: "))
    status_anggota = input("Anggota Member True / False ").lower() == "true"

    print(f"Nama mu: {nama}")
    print(f"Umur mu: {umur}")
    print(f"Tinggi mu: {tinggi_badan}")
    print(f"Status Member: {status_anggota}")


    batasan_umur = (umur >= 12) and (tinggi_badan >= 140)
    normal = (status_anggota == True) or (tinggi_badan > 160)
    tidak_boleh = not (tinggi_badan < 120 )

    print(f"Memenuhi Syarat Minimal: {batasan_umur}")
    print(f"Akses Jalur VIP: {normal}")
    print(f"Boleh naik Mandiri: {tidak_boleh}")

    if umur < 6:
        Kategori = "Kategori Balita"
        Harga = 0

    elif umur <= 11:
        Kategori = "Kategori Anak Anak"
        Harga = 5000
        if normal:
            Harga = Harga / 2
            if tidak_boleh == False:
                print("Wajib pakai pengawas")
            elif tidak_boleh == True:
                print("Tidak Wajib pakai pengawas")


    elif umur <= 19:
        Kategori = "Kategori Remaja"
        Harga = 10000
        if normal:
            Harga = Harga / 2
            if tidak_boleh == False:
                print("Wajib pakai pengawas")
            elif tidak_boleh == True:
                print("Tidak Wajib pakai pengawas")

    elif umur <= 35:
        Kategori = "Kategori Dewasa"
        Harga = 20000
        if normal:
            Harga = Harga / 2
            if tidak_boleh == False:
                print("Wajib pakai pengawas")
            elif tidak_boleh == True:
                print("Tidak Wajib pakai pengawas")
    elif umur <= 70:
        Kategori = "Kategori Tua"
        Harga = 15000
        if normal:
            Harga = Harga / 2
            if tidak_boleh == False:
                print("Wajib pakai pengawas")
            elif tidak_boleh == True:
                print("Tidak Wajib pakai pengawas")
    elif umur <= 70:
        Kategori = "Kategori Tua"
        Harga = 15000
        if normal:
            Harga = Harga / 2
            if tidak_boleh == False:
                print("Wajib pakai pengawas")
            elif tidak_boleh == True:
                print("Tidak Wajib pakai pengawas")
    elif umur <= 0:
        print("tidak valid")
    else:
        print("gak tau jir bener apa salah")


    print(f"Umur Kamu {umur} dan kamu {Kategori} mendapatkan harga {Harga} Akses {normal} Izin {tidak_boleh}")
print("selesai")



