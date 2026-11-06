#a. Buatlah dictionary bernama keranjang dengan data harga buah berikut: {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}
#b. Gunakan perulangan untuk menampilkan setiap barang dan harganya dengan format: "Harga apel: Rp 5000" 
#c. Tampilkan total belanja

#a. membuat dict data_harga_buah
data_harga_buah = {
    "apel" : 5000,
    "pisang" : 3000,
    "jeruk" : 7000,
    "anggur" : 15000,
}
print(data_harga_buah)

#b. pakai perulangan menampilkan setiap barang dan harga

items = data_harga_buah.items()
print(f"items = {items}")


for key, value in data_harga_buah.items():
    print(f"Harga = {key} : Rp.{value}") 

#c. Tampilkan total belanja
total_belanja = sum(data_harga_buah.values())
print(f"Total belanja = Rp.{total_belanja}")