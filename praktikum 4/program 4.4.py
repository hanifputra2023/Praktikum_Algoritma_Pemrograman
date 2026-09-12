#elif = else if statement, digunakan untuk menambahkan kondisi lain jika kondisi sebelumnya tidak terpenuhi.

nama = input("Nama saya: ")

#if kondisi:
#  aksi true
#elif kondisi:
#  aksi true
#elif kondisi:
#  aksi true
#else:
#  aksi 

if nama == "Hanif Putra": #kondisi
    print("Nama saya", nama, "dan saya adalah seorang mahasiswa")
elif nama == "Hanif": #kondisi
    print("Nama saya", nama, "dan saya adalah seorang mahasiswa Engineering")
elif nama == "Putra": #kondisi
    print("Nama saya", nama, "dan saya adalah seorang mahasiswa Informatika")
else: #kondisi
    print("Nama saya", nama, "dan saya bukan seorang mahasiswa")
print("================================")    