n = int(input())

mx = 0
while n > 0:
    mx = max(mx, n % 10)
    n //= 10

print(mx)