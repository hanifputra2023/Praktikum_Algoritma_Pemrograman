
nama = input("Masukkan Nama: ")
umur = int(input("Masukkan Umur: "))
tinggi_badan = float(input("Masukkan Tinggi Badan: "))
status_anggota = input("Anggota Member True / False ").lower() == "true"

print(f"Nama mu: {nama}")
print(f"Umur mu: {umur}")
print(f"Tinggi mu: {tinggi_badan}")
print(f"Status Member: {status_anggota}")

batasan_umur = (umur >= 12) and (tinggi_badan >= 140)
normal = (status_anggota == True) or (tinggi_badan > 160)
tidak_boleh = not (tinggi_badan < 120)

print(f"Memenuhi Syarat Minimal: {batasan_umur}")
print(f"Akses Jalur VIP: {normal}")
print(f"Boleh naik Mandiri: {tidak_boleh}")