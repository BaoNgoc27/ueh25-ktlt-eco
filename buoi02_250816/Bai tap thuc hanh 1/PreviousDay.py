# Input
d = int(input())
m = int(input())
y = int(input())

# Process
def is_leap(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def days_in_month(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        return 29 if is_leap(y) else 28

def previous_day(d, m, y):
    if d > 1:
        return d - 1, m, y
    else:  # d == 1
        if m == 1:            # ngày đầu năm
            return 31, 12, y - 1
        else:                  # ngày đầu tháng
            return days_in_month(m - 1, y), m - 1, y

pd, pm, py = previous_day(d, m, y)

# Output
print(f"Previous day of {d}/{m}/{y} is {pd}/{pm}/{py}.")