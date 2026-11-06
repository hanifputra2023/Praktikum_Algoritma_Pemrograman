# looping Dictionary
teman_teman = {
    "cup" : "ucup gokil",
    "tg" : "Trigeal gokil",
    "hg" : "Harley gokil",
    "zg" : "Zilong gokil",
}
#looping first try (yang keluar hanya key)
for teman in teman_teman:
    print(teman)

#operator untuk mengambil item
keys = teman_teman.keys()
print(f"keys = {keys}")

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(f"values = {values}")

for value in teman_teman.values():
    print(value)

items = teman_teman.items()
print(f"items = {items}")

for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f"key = {key} value = {value}")