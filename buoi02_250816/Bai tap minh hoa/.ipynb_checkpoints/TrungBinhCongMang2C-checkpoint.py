import sys

# Đọc n, m
n, m = map(int, sys.stdin.readline().split())
# Đọc ma trận n x m
A = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]

# Lọc các số dương và tính trung bình
positives = [x for row in A for x in row if x > 0]
if positives:
    avg = sum(positives) / len(positives)
    print(f"Trung binh cong cac so duong: {avg:.3f}.")
else:
    print("Khong co so duong trong ma tran.")
