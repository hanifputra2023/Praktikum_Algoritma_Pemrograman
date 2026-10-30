# --- SIMULASI MESIN ATM INTERAKTIF (NESTED IF) ---

# Data Akun Pengguna
PIN_BENAR = "123456"
status_akun = "aktif"   # Opsi: "aktif", "terblokir"
saldo = 1000000          # Saldo awal Rp1.000.000

print("====================================")
print("       SELAMAT DATANG DI ATM        ")
print("====================================")

# Input PIN dari pengguna
input_pin = input("Masukkan 6 digit PIN Anda: ")

# NESTED IF LEVEL 1: Cek Status Akun
if status_akun == "aktif":
    
    # NESTED IF LEVEL 2: Cek Kebenaran PIN
    if input_pin == PIN_BENAR:
        print("\n--- LOGIN BERHASIL ---")
    while True:
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Menambahkan Saldo")
        print("4. transfer")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        # NESTED IF LEVEL 3: Cek Pilihan Menu
        if pilihan == "1":
            print(f"\n[INFO] Saldo Anda saat ini: Rp{saldo:,}")
            
        elif pilihan == "2":
            nominal_tarik = int(input("\nMasukkan nominal penarikan: Rp"))
            
            # NESTED IF LEVEL 4: Cek Minimal Penarikan (Rp50.000)
            if nominal_tarik >= 50000:
                
                # NESTED IF LEVEL 5: Cek Syarat Kelipatan Rp50.000
                if nominal_tarik % 50000 == 0:
                    
                    # NESTED IF LEVEL 6: Cek Kecukupan Saldo
                    if nominal_tarik <= saldo:
                        saldo -= nominal_tarik
                        print(f"\n[BERHASIL] Penarikan sebesar Rp{nominal_tarik:,} berhasil!")
                        print(f"[INFO] Sisa saldo Anda: Rp{saldo:,}")
                    else:
                        print("\n[GAGAL] Saldo Anda tidak mencukupi untuk penarikan ini.")
                else:
                    print("\n[GAGAL] Penarikan harus kelipatan Rp50.000 (contoh: 50000, 100000, 150000).")
            else:
                print("\n[GAGAL] Penarikan minimal adalah Rp50.000.")
        elif pilihan == "3":
            nominal_tambah = int(input("\nMasukkan nominal penambahan saldo: Rp"))
            saldo += nominal_tambah
            print(f"\n[BERHASIL] Penambahan saldo sebesar Rp{nominal_tambah:,} berhasil!")
            print(f"[INFO] Saldo Anda saat ini: Rp{saldo:,}")
        elif pilihan == "4":
            nominal_transfer = int(input("\nMasukkan nominal transfer: Rp"))
            rekening_tujuan = input("Masukkan nomor rekening tujuan: ")
            
            # NESTED IF LEVEL 4: Cek Minimal Transfer (Rp50.000)
            if nominal_transfer >= 50000:
                
                # NESTED IF LEVEL 5: Cek Syarat Kelipatan Rp50.000
                if nominal_transfer % 50000 == 0:
                    
                    # NESTED IF LEVEL 6: Cek Kecukupan Saldo
                    if nominal_transfer <= saldo:
                        saldo -= nominal_transfer
                        print(f"\n[BERHASIL] Transfer sebesar Rp{nominal_transfer:,} ke rekening {rekening_tujuan} berhasil!")
                        print(f"[INFO] Sisa saldo Anda: Rp{saldo:,}")
                    else:
                        print("\n[GAGAL] Saldo Anda tidak mencukupi untuk transfer ini.")
                else:
                    print("\n[GAGAL] Transfer harus kelipatan Rp50.000 (contoh: 50000, 100000, 150000).")
            else:
                print("\n[GAGAL] Transfer minimal adalah Rp50.000.")
                
        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan layanan ATM kami. Sampai jumpa!")
            break  # Keluar dari loop while untuk mengakhiri program
        else:
            print("\n[GAGAL] Pilihan menu tidak valid.")
            
    else:
        print("\n[AKSES DITOLAK] PIN yang Anda masukkan salah!")
        
else:
    print("\n[AKSES DITOLAK] Akun Anda sedang terblokir. Silakan hubungi Customer Service.")