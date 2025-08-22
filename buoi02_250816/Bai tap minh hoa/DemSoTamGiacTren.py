import sys

# Đọc n (ma trận vuông n x n)
n = int(sys.stdin.readline())

# Đọc ma trận số thực
A = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]

eps = 1e-9
neg = pos = zero = 0

# Tam giác TRÊN của CHÉO CHÍNH: các phần tử thỏa i < j (không tính đường chéo chính)
for i in range(n):
    for j in range(i + 1, n):
        x = A[i][j]
        if x > eps:
            pos += 1
        elif x < -eps:
            neg += 1
        else:
            zero += 1

print("Trong nua tam giac tren cheo chinh:")
print(f"+ {neg} so am")
print(f"+ {pos} so duong")
print(f"+ {zero} so khong")
