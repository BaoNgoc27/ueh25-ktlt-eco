import sys

# Đọc n (ma trận vuông n x n)
n = int(sys.stdin.readline())

# Đọc ma trận số thực
A = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]

# Tam giác trên CHÉO CHÍNH: các phần tử có i < j
tg_chinh = []
for i in range(n):
    for j in range(i + 1, n):
        tg_chinh.append(A[i][j])

# Tam giác trên CHÉO PHỤ: các phần tử có j < n-1-i (không tính phần tử trên chéo phụ)
tg_phu = []
for i in range(n):
    for j in range(0, n - 1 - i):
        tg_phu.append(A[i][j])

# In kết quả (dùng định dạng 'g' để bỏ .0 nếu là số nguyên)
fmt = lambda x: f"{x:g}"
print("Tam giac tren cheo chinh: " + " ".join(fmt(x) for x in tg_chinh))
print("Tam giac tren cheo phu: " + " ".join(fmt(x) for x in tg_phu))