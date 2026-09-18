print("===mencetak bilangan prima dari 1 sampai 100")

for angka in range(2, 101):
    angka_prima = True
    for dibagi in range(2, angka):
        if angka % dibagi == 0:
            angka_prima = False
            break
    if angka_prima:
        print(angka, "adalah Bilangan Prima")