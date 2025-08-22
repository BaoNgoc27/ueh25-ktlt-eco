import sys

n = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Các đường song song CHÉO CHÍNH (i - j không đổi)
cheo_chinh_groups = []
# Bắt đầu từ hàng 0, cột n-1 về 0
for sj in range(n-1, -1, -1):
    i, j, cur = 0, sj, []
    while i < n and j < n:
        cur.append(A[i][j])
        i += 1; j += 1
    cheo_chinh_groups.append(cur)
# Sau đó từ hàng 1..n-1 ở cột 0
for si in range(1, n):
    i, j, cur = si, 0, []
    while i < n and j < n:
        cur.append(A[i][j])
        i += 1; j += 1
    cheo_chinh_groups.append(cur)

# Các đường song song CHÉO PHỤ (i + j không đổi)
cheo_phu_groups = []
# Bắt đầu từ cột 0, hàng 0..n-1 (đi lên-phải)
for si in range(0, n):
    i, j, cur = si, 0, []
    while i >= 0 and j < n:
        cur.append(A[i][j])
        i -= 1; j += 1
    cheo_phu_groups.append(cur)
# Sau đó từ hàng n-1, cột 1..n-1
for sj in range(1, n):
    i, j, cur = n-1, sj, []
    while i >= 0 and j < n:
        cur.append(A[i][j])
        i -= 1; j += 1
    cheo_phu_groups.append(cur)

fmt_group = lambda g: "[" + ", ".join(map(str, g)) + "]"
print("Cac duong song song cheo chinh: " + "".join(fmt_group(g) for g in cheo_chinh_groups))
print("Cac duong song song cheo phu: "   + "".join(fmt_group(g) for g in cheo_phu_groups))
