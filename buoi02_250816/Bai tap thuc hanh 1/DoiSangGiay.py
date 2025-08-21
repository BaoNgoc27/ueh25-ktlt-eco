# DoiSangGiay.py

# Nhập số giờ, phút, giây
h = int(input("Nhap so gio: "))
m = int(input("Nhap so phut: "))
s = int(input("Nhap so giay: "))

# Tính tổng số giây
tong = h * 3600 + m * 60 + s

print(f"Tong so giay cua {h}:{m}:{s} la {tong} giay")
