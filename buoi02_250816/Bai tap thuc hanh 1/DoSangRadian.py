# DoSangRadian.py
import math

# Nhập góc độ
degree = float(input("Nhap goc (do): "))

# Đổi sang radian: rad = degree * pi / 180
radian = math.radians(degree)

print(f"{degree} do = {radian:.4f} radian")
