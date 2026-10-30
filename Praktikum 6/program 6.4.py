## For in While
# for_in_while.py
sesi = 1
while sesi <= 2:  # Outer while: mengontrol nomor sesi
    print(f"Sesi ke-{sesi}:")
    
    # Inner for: mencetak nomor antrean pada sesi tersebut
    for antrean in range(1, 4):
        print(f"  Melayani pasien nomor: {antrean}")
        
    sesi = sesi + 1  # Increment sesi untuk iterasi berikutnya
    print("---")