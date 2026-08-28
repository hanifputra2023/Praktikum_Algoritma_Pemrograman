print("Hello World");

#Variable adalah tempat menyimpan sebuah data
#menaruh / assignment nilai
#di python tidak perlu di deklarasi

a = 10
x = 5
panjang = 1000

#pemanggilan pertama
print("Nilai A: ", a)
print("Nilai X: ", x)
print("Nilai Panjang: ", panjang)
print("================================")
#penamaan
nilai_y = 15 #dengan menggunaan underscore
nilaiZ = 20 #dengan menggunakan camel case
jumlahTotal15 = 30

#pemanggilan kedua
print("Nilai a = ", a)
a = 7
print("Nilai a = ", a)

b = a
print("Nilai b = ", b)
print("================================")

# a = 10, a adalah variable dengan nilai 10
#tipe data: Angka satuan yang gak ada komanya(interger)
data_interger = 1
print("data interger: ", data_interger)
print("tipe data: ", type(data_interger))
print("================================")
#tipe data: Angka dengan koma (float)
data_float = 1.5
print("data float: ", data_float)
print("tipe data: ", type(data_float))
print("================================")
#tipe_data: Kumpulan karakter (string)
data_string = "Hanif"
print("data string: ", data_string)
print("tipe data: ", type(data_string))
print("================================")
#tipe data: biner True/False (boolean)
data_boolean = True
print("data boolean: ", data_boolean)
print("tipe data: ", type(data_boolean))
print("================================")
#tipe data: khusus

#bilangan Kompleks
data_kompleks = complex(5,6)
print("data kompleks: ", data_kompleks)
print("tipe data: ", type(data_kompleks))
print("================================")

#tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data c_double: ", data_c_double)
print("tipe data: ", type(data_c_double))
print("================================")

#kita belajar Casting, yaitu mengubah tipe data ke tipe data lain
#tipe data = int, float, str, bool

#interger ke tipe data lain
data_int = 9
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0
print("data = ", data_float, " bertipe = ", type(data_float))
print("data = ", data_str, " bertipe = ", type(data_str))
print("data = ", data_bool, " bertipe = ", type(data_bool))

#Float ke tipe data lain
data_float = 9.5
data_int = int(data_float) #akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika nilai float = 0
print("data = ", data_int, " bertipe = ", type(data_int))
print("data = ", data_str, " bertipe = ", type(data_str))
print("data = ", data_bool, " bertipe = ", type(data_bool))

#strng ke tipe data lain
data_str = "10"
data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str) #akan false jika string kosong
print("data = ", data_int, " bertipe = ", type(data_int))
print("data = ", data_float, " bertipe = ", type(data_float))
print("data = ", data_bool, " bertipe = ", type(data_bool))

#input data user
#data yang dimasukkan pasti string
Nama = input("Siapa nama anda: ")
print("Nama anda adalah: ", Nama, " dan bertipe data: ", type(Nama))

#jika kita ingin mengambil int, maka
Nilai = int(input("Masukkan nilai: "))
print("Nilai anda adalah: ", Nilai, " dan bertipe data: ", type(Nilai))

#variable adalah tempat untuk menyimpan data, dan data yang disimpan bisa diubah-ubah