d = int(input())
m = int(input())
y = int(input())

def is_leap(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def days_in_month(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        return 29 if is_leap(y) else 28

def next_day(d, m, y):
    if d < days_in_month(m, y):
        return d + 1, m, y
    else:
        if m == 12:
            return 1, 1, y + 1
        else:
            return 1, m + 1, y

nd, nm, ny = next_day(d, m, y)
print(f"{nd}/{nm}/{ny}")