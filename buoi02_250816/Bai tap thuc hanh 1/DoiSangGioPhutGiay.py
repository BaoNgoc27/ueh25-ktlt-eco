# DoiSangGioPhutGiay.py

# Nhập tổng số giây
tong = int(input("Nhap vao tong so giay: "))

# Tính giờ, phút, giây
h = tong // 3600
m = (tong % 3600) // 60
s = tong % 60

print(f"{tong} giay co dang {h}:{m}:{s}")