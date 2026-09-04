#Operasi Komperasi

#setiap hasil dari operasi komperasi adalah boolean (True atau False)

a = 10
b = 3

#Operasi Lebih Besar Dari >
print("===Operasi Lebih Besar Dari (>)===")
hasil = a > b
print(a, ">", b, "=", hasil)
hasil = b > a
print(b, ">", a, "=", hasil)
hasil = a > 3
print(a, ">", 3, "=", hasil)
hasil = b > 3
print(b, ">", 3, "=", hasil)
hasil = b > 2
print(b, ">", 2, "=", hasil)

#Operasi Lebih Kecil Dari <
print("===Operasi Lebih Kecil Dari (<)===")
hasil = a < b
print(a, "<", b, "=", hasil)
hasil = b < a
print(b, "<", a, "=", hasil)
hasil = a < 3
print(a, "<", 3, "=", hasil)
hasil = b < 3
print(b, "<", 3, "=", hasil)
hasil = b < 2
print(b, "<", 2, "=", hasil)

#Operasi Lebih Besar Sama Dengan >=
print("===Operasi Lebih Besar Sama Dengan (>=)===")
hasil = a >= b
print(a, ">=", b, "=", hasil)
hasil = b >= a
print(b, ">=", a, "=", hasil)
hasil = a >= 3
print(a, ">=", 3, "=", hasil)
hasil = b >= 3
print(b, ">=", 3, "=", hasil)
hasil = b >= 2
print(b, ">=", 2, "=", hasil)

#Operasi Lebih Kecil Sama Dengan <=
print("===Operasi Lebih Kecil Sama Dengan (<=)===")
hasil = a <= b
print(a, "<=", b, "=", hasil)
hasil = b <= a
print(b, "<=", a, "=", hasil)
hasil = a <= 3
print(a, "<=", 3, "=", hasil)
hasil = b <= 3
print(b, "<=", 3, "=", hasil)
hasil = b <= 2
print(b, "<=", 2, "=", hasil)

#Operasi Sama Dengan ==
print("===Operasi Sama Dengan (==)===")
hasil = a == b
print(a, "==", b, "=", hasil)
hasil = b == a
print(b, "==", a, "=", hasil)
hasil = a == 3
print(a, "==", 3, "=", hasil)
hasil = b == 3
print(b, "==", 3, "=", hasil)
hasil = b == 2
print(b, "==", 2, "=", hasil)


#Operasi Tidak Sama Dengan !=
print("===Operasi Tidak Sama Dengan (!=)===")
hasil = a != b
print(a, "!=", b, "=", hasil)
hasil = b != a
print(b, "!=", a, "=", hasil)
hasil = a != 3
print(a, "!=", 3, "=", hasil)
hasil = b != 3
print(b, "!=", 3, "=", hasil)
hasil = b != 2
print(b, "!=", 2, "=", hasil)

# "is" sebagai komparasi object identity, mengecek apakah kedua object itu sama atau tidak
print("===Operasi is===")
x = 5 #ini adalah assignment membuat objek, bukan perbandingan
y = 5
hasil = x is y
print(x, "is", y, "=", hasil)

x = 5 #ini adalah assignment membuat objek, bukan perbandingan
y = 6
hasil = x is y
print(x, "is", y, "=", hasil)

# "is not" sebagai komparasi object identity, mengecek apakah kedua object itu tidak sama
print("===Operasi is not===")
x = 5 #ini adalah assignment membuat objek, bukan perbandingan
y = 5
hasil = x is not y
print(x, "is not", y, "=", hasil)
