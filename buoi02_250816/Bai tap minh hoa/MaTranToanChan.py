import sys

# Đọc n, m
n, m = map(int, sys.stdin.readline().split())

# Đọc ma trận n dòng, mỗi dòng m số nguyên
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Kiểm tra toàn chẵn
all_even = all(x % 2 == 0 for row in A for x in row)

if all_even:
    print("Mang A toan chan!")
else:
    print("Mang A khong toan chan!")
