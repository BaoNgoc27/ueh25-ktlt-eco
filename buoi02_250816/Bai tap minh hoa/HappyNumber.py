import sys

def sum_of_squares(n: int) -> int:
    s = 0
    while n > 0:
        n, d = divmod(n, 10)
        s += d * d
    return s

data = sys.stdin.read().strip().split()
n = int(data[0])

seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    n = sum_of_squares(n)

print("True" if n == 1 else "False")
