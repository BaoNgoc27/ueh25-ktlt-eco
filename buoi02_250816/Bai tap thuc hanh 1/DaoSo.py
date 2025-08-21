# DaoSo.py

# Nhập số nguyên x có 4 chữ số
x = int(input("Nhap so nguyen co 4 chu so: "))

# Đảo số bằng cách chuyển sang chuỗi
y = int(str(x)[::-1])

print(f"So dao cua {x} la {y}")
