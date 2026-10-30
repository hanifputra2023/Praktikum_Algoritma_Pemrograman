# seorang dosen ingin membuat program otomatis untuk
# 1. memeriksa apakah seorang mahasiswa berhak mengikutin
# ujian akhir semester (UAS)
# berdasarkan nilai persentase kehadiran dan kelengkapan tugas.
# 2. menentukan grade nilai akhir ( A, B, C, D,E) berserta status
# kelulusannya menggunakan kombinasi rentang nilai dan 
# operator logika

nama = input("Masukkan Nama: ")
status = input("Sudah Komplit dalam Mengumpulkan Tugas?: ").lower() == "true"
kehadiran = int(input("Kehadiran Dalam Persen; "))


if status == True:
    nilai_MTK = float(input("Nilai Matematika: "))
    nilai_Bahasa = float(input("Nilai Bahasa Indo: "))
    nilai_Pemrograman = float(input("Nilai Pemrograman: "))

else:
    print("anda tidak dapat mengikutin UAS tugas belum komplit")


rata_nilai = (nilai_MTK + nilai_Bahasa + nilai_Pemrograman) / 3
uas = (rata_nilai >= 80 ) and (kehadiran >= 80 )
nilai_akhir = (rata_nilai)

if uas:
    print("Bisa mengikutin UAS")
    nilai_uas = float(input("Nilai UAS: "))
else:
    print("Tidak bisa mengikutin uas")

if uas >