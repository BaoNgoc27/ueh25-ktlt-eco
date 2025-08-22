import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
nums = data[1:1+n]          # lấy đúng n số đầu tiên

candidate = None
count = 0
for x in nums:
    if count == 0:
        candidate = x
        count = 1
    elif x == candidate:
        count += 1
    else:
        count -= 1

print(candidate)
