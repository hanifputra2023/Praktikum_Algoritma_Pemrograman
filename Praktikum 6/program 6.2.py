## Nested While
i = 1
while i <= 2:
    j = 1
    while j <= 3:
        print("Teknologi Informasi")
        j = j + 1
    print("\n") # Mencetak baris baru (\n) saat inner loop selesai
    i = i + 1

## --- Nested While
i = 1
N = 1
while i <= 2:
    j = 1
    while j <= 3:
        print(N)
        N = N + 2
        j = j + 1
    i = i + 1