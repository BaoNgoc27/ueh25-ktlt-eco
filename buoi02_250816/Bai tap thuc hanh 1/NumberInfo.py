n = int(input())

digits = [int(ch) for ch in str(n)]
num_digits = len(digits)
sum_digits = sum(digits)
last_digit = digits[-1]
first_digit = digits[0]

print(f"{n} has {num_digits} digits.")
print(f"1 + 5 + 6 = {sum_digits}.")
print(f"Last digit is {last_digit}.")
print(f"Fist digit is {first_digit}.")