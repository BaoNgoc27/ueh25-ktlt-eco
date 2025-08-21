a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("Unlimited solutions")
        else:
            print("No solution")
    else:
        x = -c / b
        print(f"x1={x:.2f}")
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("No solution")
    elif delta == 0:
        x = -b / (2*a)
        print(f"x1={x:.2f}")
    else:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        print(f"x1={x1:.2f}, x2={x2:.2f}")