#continue, pass, break

#pass dia berfungsi untuk menandai bahwa blok kode tersebut tidak akan dijalankan, tetapi tetap valid secara sintaksis. Biasanya digunakan sebagai placeholder.

angka = 0

while angka < 5:
    angka = angka + 1
    if angka == 3:
        pass # akan membuat loop tetap berjalan   
    print(f"angka sekarang adalah {angka}")

 
#continue 
 
angka = 0 
print(f"angka sekarang → {angka}") 
 
while angka < 5: 
    angka = angka + 1 
    print(f"angka sekarang → {angka}") # aksi 1 
    
    if(angka == 3): 
         print("nice") 
         continue # akan membuat loop meloncat ke step selanjutnya 
    print("whasssup") # aksi 2 
    
print("Pinish")