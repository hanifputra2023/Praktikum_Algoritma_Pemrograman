#a. Buatlah sebuah dictionary bernama data_mahasiswa dengan pasangan key-value berikut: - "nim": "240101" - "nama": "Budi Santoso" - "prodi": "Teknologi Informasi"
#b. ubah nilai "prodi" menjadi "Sistem Informasi" sekaligus menambah key baru "angkatan" dengan nilai "2026"
#c. Hapus data "nim", lalu tampilkan hasil akhir dictionary ke layar

#a. Membuat dictionary bernama data_mahasiswa
data_mahasiswa = {
    "nim" : "2605060054",
    "nama" : "Nanda Hanif Abyan Bromo Putra",
    "prodi" : "Teknologi Informasi"
}
print(data_mahasiswa)

#b. ubah nilai prodi menjadi Sistem Informasi dan menambahkan key baru angkatan dengan nilai 2026
data_mahasiswa.update({
    "prodi" : "Sistem Informasi",
    "angkatan" : 2026,
})
print(data_mahasiswa)

#c. menghapus data nim dan tampilkan hasil akhirnya
del data_mahasiswa["nim"]
print(data_mahasiswa)