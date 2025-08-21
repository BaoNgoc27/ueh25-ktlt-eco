# Input
old = int(input())   # chỉ số cũ
new = int(input())   # chỉ số mới

# số kWh tiêu thụ
kWh = new - old

# Process
def calc_price(kWh):
    price = 0
    if kWh <= 100:
        price = kWh * 1242
    elif kWh <= 150:
        price = 100 * 1242 + (kWh - 100) * 1304
    elif kWh <= 200:
        price = 100 * 1242 + 50 * 1304 + (kWh - 150) * 1651
    elif kWh <= 300:
        price = 100 * 1242 + 50 * 1304 + 50 * 1651 + (kWh - 200) * 1788
    elif kWh <= 400:
        price = 100 * 1242 + 50 * 1304 + 50 * 1651 + 100 * 1788 + (kWh - 300) * 1912
    else:
        price = 100 * 1242 + 50 * 1304 + 50 * 1651 + 100 * 1788 + 100 * 1912 + (kWh - 400) * 1962

    # cộng VAT 10%
    price = int(price * 1.1)
    return price

ans = calc_price(kWh)

# Output
print(f"The amount to pay for {kWh} kWh consumed in the month is {ans:,} VND.")
