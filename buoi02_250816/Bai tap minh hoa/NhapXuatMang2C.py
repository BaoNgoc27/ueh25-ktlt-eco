# NhapXuatMang2C.py

# Đọc n, m
n, m = map(int, input().split())

# Đọc ma trận A
A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Xuất ma trận
print("Array A:")
for row in A:
    print(*row)
