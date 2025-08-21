# Input
a = int(input())
b = int(input())
c = int(input())

# Process
def is_triangle(a, b, c):
    x, y, z = sorted([a, b, c])   # x <= y <= z
    return x + y > z

def max_side(a, b, c):
    return max(a, b, c)

# Output
if is_triangle(a, b, c):
    print("a, b, c tạo thành tam giác")
else:
    m = max_side(a, b, c)
    print(f"Max({a}, {b}, {c})= {m}.")