#id dan else statment
#1. if nya
#2. kondisinya
#3. aksinya

nama = input("Nama saya: ")

#1. program if inline
if nama == "Hanif Putra": print("Nama saya", nama, "dan saya adalah seorang mahasiswa")
print("================================")

#2. program if indentation
if nama == "Hanif Putra":
    print("Nama saya", nama, "dan saya adalah seorang mahasiswa")
    print(nama, "Kamu Jago Sekali")
print("================================")

#3. else statement
if nama == "Hanif Putra":
    print("Nama saya", nama, "dan saya adalah seorang mahasiswa")
else:
    print("Nama saya", nama, "dan saya bukan seorang mahasiswa")
print("================================")
