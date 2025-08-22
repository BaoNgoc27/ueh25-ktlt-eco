import sys

# Đọc số dòng n
n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().rstrip("\n")
    words = s.split()                 # tách theo khoảng trắng (tự bỏ dư thừa)
    print(" ".join(reversed(words)))  # đảo thứ tự từ và in ra
