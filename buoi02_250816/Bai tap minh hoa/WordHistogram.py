import sys, re
from collections import Counter

# Đọc số câu
n = int(sys.stdin.readline())

# Gom tất cả từ (không phân biệt hoa/thường), tách theo space và dấu câu
# Giữ lại toàn bộ ký tự chữ cái có dấu tiếng Việt
words = []
for _ in range(n):
    line = sys.stdin.readline().strip()
    words += [w.lower() for w in re.findall(r"[A-Za-zÀ-ỹĐđ]+", line)]

# Đếm tần số
cnt = Counter(words)

# In theo: (1) tần suất giảm dần, (2) rồi từ điển (Unicode) tăng dần
for w, c in sorted(cnt.items(), key=lambda x: (-x[1], x[0])):
    print(f"{w}: {c}")