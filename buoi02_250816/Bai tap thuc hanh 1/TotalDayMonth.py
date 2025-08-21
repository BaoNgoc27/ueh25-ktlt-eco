m = int(input())
y = int(input())

def is_leap(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

if m in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif m in [4, 6, 9, 11]:
    days = 30
elif m == 2:
    days = 29 if is_leap(y) else 28

print(days)