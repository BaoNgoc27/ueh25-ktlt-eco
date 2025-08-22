import sys

# Đọc n (ma trận vuông n x n)
n = int(sys.stdin.readline())

# Đọc ma trận
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Lấy các phần tử trên chéo chính và chéo phụ
cheo_chinh = [A[i][i] for i in range(n)]
cheo_phu   = [A[i][n-1-i] for i in range(n)]

# In kết quả
print("Cac phan tu tren cheo chinh: " + " ".join(map(str, cheo_chinh)))
print("Cac phan tu tren cheo phu: " + " ".join(map(str, cheo_phu)))
