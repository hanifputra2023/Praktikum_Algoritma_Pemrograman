# Kumpulan data numbers
data_angka = [1, 2, 3, 4, 5]
print("Data angka:", data_angka)

# Kumpulan data string
data_string = ["Alice", "Bob", "Charlie", "David"]
print("Data string:", data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, False]
print("Data boolean:", data_boolean)

# Kumpulan data campuran
data_campuran = [1, "bakwan", 2, "tahu", 3, "tempe"]
print("Data campuran:", data_campuran)

## Cara alternatif membuat list
data_range = range(0, 10, 2) # range(start, stop, step)
data_list = list(data_range)
data_list = list(range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_for = [i **2 for i in range(0, 10)]
print(list_for)

# Membuat list dengan for dan if
list_for_if = [i for i in range(0, 10) if i != 5]
print(list_for_if)

list_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0, 10) if i % 2 != 0]
print(list_for_if)
