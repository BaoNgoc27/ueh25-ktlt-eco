# HamSo1.py
import math

# Nhập số thực x
x = float(input("Nhap so thuc x: "))

# Tính y1 và y2
y1 = 4 * (x**2 + 10 * math.sqrt(x) + 3 * x + 1)
y2 = (math.sin(x**2) + math.sqrt(x**2 + 1)) / (math.exp(2*x) + math.cos((math.pi/4) * x))

print(f"y1 = {y1:.2f}")
print(f"y2 = {y2:.2f}")
