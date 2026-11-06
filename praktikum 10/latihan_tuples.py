#a.Buatlah sebuah Tuple bernama mahasiswa yang berisi 3 data diri Anda: ("Nama", "NIM", "Prodi").
#b. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya. 
#c. Coba jalankan kode mahasiswa[2] = "Teknologi Informasi". Amati pesan error yang muncul, lalu jelaskan mengapa hal tersebut terjadi 
#d. Buatlah sebuah Set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5. Cetak nilai_angka ke layar dan jelaskan apa yang terjadi pada angka 10 dan 4 yang ditulis dua kali!

# a. Membuat Tuple bernama mahasiswa
mahasiswa = ("Nanda Hanif Abyan Bromo Putra", 2605060054, "Teknologi Informasi")
print(f"mahasiswa = {mahasiswa}")

# b. Menampilkan data NIM dan Prodi ke layar
print(f"NIM: {mahasiswa[1]}")
print(f"Prodi: {mahasiswa[2]}")

# c. Coba jalankan kode mahasiswa[2] = "Teknologi Informasi"
# mahasiswa[2] = "Teknologi Informasi"  
## Pesan error yang muncul adalah "TypeError: 'tuple' object does not support item assignment". Hal ini terjadi karena Tuple bersifat immutable, artinya data di dalam Tuple tidak dapat diubah setelah dibuat. Oleh karena itu, kita tidak bisa mengubah nilai pada indeks tertentu dari Tuple.

# d. Membuat Set bernama nilai_angka
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(f"nilai_angka = {nilai_angka}")
#pada set, angka 10 dan 4 itu cuma di tulis 1 kali saja, karena dalam set atau himpunan, setiap elemen harus unik, jadi meskipun kita memasukkan angka  4 dan 10 itu beberapa kali di dalam set, hanya satu nilai yang akan disimpan.

