#latihan logika dan komparasi
#membuat gabungan area tentang rentang dari angka
#+++++3====10+++++
inputUser = float(input("Masukkan angka yang bernilai \nkurang dari 3 \natau lebih besar dari 10\n: "))
print("biasa")
#+++++3------
#memeriksa angka kurang dari 3
isKurangDari3 = inputUser < 3
print("Kurang dari 3 =", isKurangDari3)

#-----10+++++
#memeriksa angka lebih dari 10
isLebihDari10 = inputUser > 10
print("Lebih dari 10 =", isLebihDari10)
isCorrect = isKurangDari3 or isLebihDari10
print("angka yang anda masukkan =", isCorrect)
print("================================")

#-----3+++++10------
#kasus irisan
inputUser = float(input("Masukkan angka yang bernilai \nlebih dari 3 \ndan kurang dari 10\n: "))
print("irisan")
isLebihDari3 = inputUser > 3
print("Lebih dari 3 =", isLebihDari3)
isKurangDari10 = inputUser < 10
print("Kurang dari 10 =", isKurangDari10)
isCorrect = isLebihDari3 and isKurangDari10
print("angka yang anda masukkan =", isCorrect)