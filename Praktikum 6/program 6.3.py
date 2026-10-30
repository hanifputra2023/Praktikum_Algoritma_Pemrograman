## Nested FOR
for i in range(1, 3):       # Outer loop (baris 1 s.d. 2)
    for j in range(1, 4):   # Inner loop (kolom 1 s.d. 3)
        print(f"[{i}, {j}]", end="")
    print()                 # Pindah baris