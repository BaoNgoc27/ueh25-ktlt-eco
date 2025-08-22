import sys

# Đọc n và ma trận vuông n x n (số nguyên)
n = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Các dòng theo hình (ziczac trái→phải rồi phải→trái)
row_groups = []
for i in range(n):
    cur = A[i] if i % 2 == 0 else A[i][::-1]
    row_groups.append(cur)

# Các cột theo hình (ziczac trên→dưới rồi dưới→trên)
col_groups = []
for j in range(n):
    col = [A[i][j] for i in range(n)]
    cur = col if j % 2 == 0 else col[::-1]
    col_groups.append(cur)

fmt = lambda arr: "[" + ", ".join(map(str, arr)) + "]"
print("Cac dong: " + "".join(fmt(g) for g in row_groups))
print("Cac cot: "  + "".join(fmt(g) for g in col_groups))
