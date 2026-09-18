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