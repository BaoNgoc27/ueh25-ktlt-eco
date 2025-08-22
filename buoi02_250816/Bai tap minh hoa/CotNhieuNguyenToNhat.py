import sys, math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for p in range(3, r + 1, 2):
        if n % p == 0:
            return False
    return True

# Đọc n, m
n, m = map(int, sys.stdin.readline().split())
# Đọc ma trận n x m
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Đếm số nguyên tố theo cột
counts = [0] * m
for j in range(m):
    for i in range(n):
        if is_prime(A[i][j]):
            counts[j] += 1

max_cnt = max(counts) if counts else 0
if max_cnt == 0:
    print("Khong co so nguyen to trong ma tran.")
else:
    cols = [str(j) for j, c in enumerate(counts) if c == max_cnt]
    print("Cac cot nhieu nguyen to nhat: " + " ".join(cols))
