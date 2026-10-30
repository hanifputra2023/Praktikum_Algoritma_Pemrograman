## Nested IF
# if kondisi_utama:
#     if kondisi_lanjutan:
#         Aksi jika kedua kondisi bernilai True
#     else:
#         Aksi jika kondisi_utama True, tetapi kondisi_lanjutan False
# else:
#     Aksi jika kondisi_utama False

status_akun = "aktif"  # pilihan: "aktif", "terblokir"
saldo = 750000
nominal_tarik = 500000

if status_akun == "aktif":
    if nominal_tarik <= saldo:
        if nominal_tarik >= 50000:
            saldo = saldo - nominal_tarik
            print(f"Penarikan berhasil: Rp{nominal_tarik:,}")
            print(f"Sisa saldo: Rp{saldo:,}")
        else:
            print("Gagal: Penarikan minimal Rp50,000.")
    else:
        print("Gagal: Saldo tidak mencukupi.")
else:
    print("Akses ditolak: Akun sedang terblokir.")