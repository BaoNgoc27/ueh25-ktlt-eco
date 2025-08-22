import sys

# Đọc n, m
n, m = map(int, sys.stdin.readline().split())

vowels = set("AEIOU")  # nguyên âm (không phân biệt hoa/thường)

best_row = -1
best_cnt = -1

for i in range(n):
    # mỗi dòng có m ký tự, cách nhau bởi khoảng trắng
    tokens = sys.stdin.readline().split()
    # đếm số nguyên âm của dòng i (không phân biệt hoa/thường)
    cnt = sum(1 for ch in tokens if ch.upper() in vowels)
    if cnt > best_cnt:
        best_cnt = cnt
        best_row = i          # theo mẫu slide: đánh số dòng kiểu 0,1,2,...

if best_cnt <= 0:
    print("Khong co nguyen am trong ma tran.")
else:
    print(f"Dong {best_row} co nhieu nguyen am nhat voi so luong nguyen am la {best_cnt}.")
