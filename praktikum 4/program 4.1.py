#operasi logika atau boolean
#not, or, and, xor
print("====NOT====")
a = True
b = not a
print(" data a =", a)
print("==========Not==========")
print(" data b =", b)

# OR (jika salah satu bernilai True maka hasilnya True)
print("====OR====")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)

a = False
b = True
c = a or b
print(a, "OR", b, "=", c)

a = True
b = False
c = a or b
print(a, "OR", b, "=", c)

a = True
b = True
c = a or b
print(a, "OR", b, "=", c)

# AND (jika salah satu bernilai False maka hasilnya False)
print("====AND====")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)

a = False
b = True
c = a and b
print(a, "AND", b, "=", c)

a = True
b = False
c = a and b
print(a, "AND", b, "=", c)

a = True
b = True
c = a and b
print(a, "AND", b, "=", c)

#XOR (jika salah satu bernilai True maka hasilnya True, jika keduanya sama maka hasilnya False)
print("====XOR====")
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)

a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c)

a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c)

a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c)  