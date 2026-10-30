# WHILE LOOP

# while loop adalah salah satu jenis perulangan dalam pemrograman yang digunakan untuk menjalankan blok kode tertentu selama kondisi yang diberikan bernilai True. Perulangan ini akan terus berlanjut hingga kondisi tersebut menjadi False. Struktur dasar dari while loop adalah sebagai berikut:
# while kondisi:
#     aksi ini
#     aksi itu

print("=== Contoh 1 While Loop ===")

angka = 10
while angka > 2:
    print("Hanif Putra Ganteng Sekali")
    
print("=== Contoh 2 While Loop ===")
angka = 0
print(f"angka sekarang adalah {angka}")

while angka < 2:
    angka = angka + 1
    #angka = angka + 1
    print(f"angka sekarang adalah {angka}")
    print("Hanif Putra Ganteng Sekali")
print("program berakhir dan Hanif Putra Tidak Ganteng Sekali")

print("=== Contoh 3 While Loop ===")

angka = 10
while angka > 2:
    print("Hanif Putra Ganteng Sekali")
    angka = angka - 1