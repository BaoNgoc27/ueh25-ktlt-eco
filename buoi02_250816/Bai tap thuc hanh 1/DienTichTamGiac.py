# DienTichTamGiac.py
import math

# Nhập độ dài 3 cạnh
a = float(input("Nhap do dai canh a: "))
b = float(input("Nhap do dai canh b: "))
c = float(input("Nhap do dai canh c: "))

# Tính nửa chu vi
p = (a + b + c) / 2

# Tính diện tích theo công thức Heron
S = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f"Dien tich tam giac S = {S:.2f}")
