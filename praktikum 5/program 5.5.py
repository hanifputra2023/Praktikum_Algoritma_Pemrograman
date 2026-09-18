# *
# * *
# * * *
# * * * *
# * * * * *

# Latihan membuat sebuah segitiga bintang

# 1. Menggunakan for 
sisi = 5
count = 1
for i in range(sisi):
    print("* " * count)
    count = count + 1

# 2. Menggunakan while

sisi = 5
count = 1

while True:
    print("* " * count)
    count = count + 1
    if count > sisi:
        break