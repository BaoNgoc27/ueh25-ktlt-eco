# SortList.py
n = int(input())
arr = [input().strip() for _ in range(n)]

# String compare
string_sorted = sorted(arr)

# Integer compare
int_sorted = sorted(arr, key=int)

print("String compare:", string_sorted)
print("Integer compare:", int_sorted)
