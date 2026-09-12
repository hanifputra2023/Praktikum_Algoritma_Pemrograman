Nama = input("Nama saya: ")
Umur = int(input("Umur saya: "))
print("================================")

if Umur >= 0 and Umur <= 12:
    print("Nama saya", Nama, "dan saya Kategori Anak-anak")
elif Umur >= 13 and Umur <= 17:
    print("Nama saya", Nama, "dan saya Kategori Remaja")
elif Umur >= 18 and Umur <= 59:
    print("Nama saya", Nama, "dan saya Kategori Dewasa")
elif Umur >= 60:
    print("Nama saya", Nama, "dan saya Kategori Lansia")
else:
    print("Umur tidak valid")