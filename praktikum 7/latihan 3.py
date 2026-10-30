data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]] 

barang_buku = ["Buku", 5000]
barang_pensil = ["Pensil", 2000]
barang_penggaris = ["Penggaris", 3000]

list_barang = [barang_buku, barang_pensil, barang_penggaris]
print(f"list barang = {list_barang}")

print("================================")
print(f"Harga Barang Pensil\t : {list_barang[1][1]}")
print("================================")
for barang in list_barang:
    print(f"Nama Barang\t : {barang[0]}")
    print(f"Harga Barang\t : {barang[1]}\n")