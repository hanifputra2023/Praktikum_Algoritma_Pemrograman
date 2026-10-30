# ipk = 3.65
# penghasilan_ortu = 4500000
# organisasi = True
for angka in range (1, 5):
    nama = input("Nama Mahasiswa: ")
    ipk = float(input("IPK Mahasiswa: "))
    organisasi = input("Aktif Organisasi (True / False) ?: ").lower() == "true"
    penghasilan_ortu = int(input("Masukkan Nominal Penghasilan: "))

    print(f"Mahasiswa: {nama}")
    print(f"IPK Mahasiswa: {ipk}" )
    print(f"Keaktifan Organisasi: {organisasi}")
    print(f"Pengahasilan Orang Tua: {penghasilan_ortu}")

    prestasi_mahasiswa = (ipk >= 3.5) and organisasi
    bantuan = (ipk >= 3.0) and (penghasilan_ortu < 5000000)

    print(f"Memenuhi Syarat Prestasi: {prestasi_mahasiswa}")
    print(f"Memenuhi Syarat bantuan: {bantuan}")
    print(f"Memenuhi Syarat Ke AKtifan Organisasi: {organisasi}")

    if ipk >= 3.8 and penghasilan_ortu <= 5000000 :
        kategori = "Beasiswa anda Menjadi (100%) gratis"
    elif (prestasi_mahasiswa) or (bantuan):
        kategori = "Beasiswa anda mendapatkan potongan (50%)"
    elif ipk > 2.5 and (organisasi):
        kategori = "Beasiswa anda mendapatkan potongan (5%)"
    else:
        kategori = "Beasiswa anda tidak mendapatkan potongan"

    print(f"Anda Masuk Rekomendasi: {kategori}")
print("selesai")


