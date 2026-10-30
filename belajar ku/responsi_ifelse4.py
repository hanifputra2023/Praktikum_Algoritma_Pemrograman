# login maksimal 3 kali
# username = nanda
# password = admin

maksimal = 3
percobaan = 0

while percobaan < maksimal:
    nama = input("Masukkan Nama: ")
    password = input("Masukkan Password: ")
    if nama == "Nanda" and password == "Admin":
        print("Login Anda Berhasil..")
        break
    
    elif percobaan < 3:
        percobaan = percobaan + 1
        sisa = maksimal - percobaan
        print(f"percobaan masih ada {sisa}")

    else:
         print(f"masa login anda {sisa}")
        

