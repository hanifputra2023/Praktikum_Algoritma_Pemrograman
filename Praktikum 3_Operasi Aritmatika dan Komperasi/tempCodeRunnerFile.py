# "is" sebagai komparasi object identity, mengecek apakah kedua object itu sama atau tidak
print("===Operasi is===")
x = 5 #ini adalah assignment membuat objek, bukan perbandingan
y = 5
hasil = x is y
print(x, "is", y, "=", hasil)

x = 5
y = 6
hasil = x is y
print(x, "is", y, "=", hasil)

# "is not" sebagai komparasi object identity, mengecek apakah kedua object itu tidak sama
print("===Operasi is not===")
x = 5 #ini adalah assignment membuat objek, bukan perbandingan
y = 5
hasil = x is not y
print(x, "is not", y, "=", hasil)