## --- Operasi Dictionary ---

data_dict = {
    "cup": "ucup surucup",
    "pet": "opet saripet",
    "ndo": "nando surundo",
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis", "key tidak ditemukan"))  # check key dengan message

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["de"] = "ade si adek"
print(data_dict)

data_dict.update({"cup": "ucup surucup"})
print(data_dict)
data_dict.update({"iwn": "iwan mang keren"})  # akan ditambah jika tidak ada
print(data_dict)

# menghapus data
del data_dict["iwn"]
print(data_dict)