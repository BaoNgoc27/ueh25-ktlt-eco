# Input
a = int(input())
b = int(input())
op = input().strip()

# Process
def calc(a, b, op):
    if op == '+':
        return f"{a} + {b} = {a + b}"
    elif op == '-':
        return f"{a} - {b} = {a - b}"
    elif op == '*':
        return f"{a} * {b} = {a * b}"
    elif op == '/':
        if b == 0:
            return "Không tính được"
        else:
            return f"{a} / {b} = {a / b}"
    else:
        return "Phép toán không hợp lệ"

ans = calc(a, b, op)

# Output
print(ans)
