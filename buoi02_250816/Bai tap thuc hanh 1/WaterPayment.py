old_index = int(input())
new_index = int(input())
people = int(input())

used = new_index - old_index
quota = people * 4
remain = used
cost = 0

if remain > 0:
    take = min(remain, quota)
    cost += take * 4400
    remain -= take
if remain > 0:
    take = min(remain, people * 2)
    cost += take * 8300
    remain -= take
if remain > 0:
    cost += remain * 10500

# Thuế VAT 5% và phí môi trường 10%
cost = cost * 1.15

print(f"Payment for {used} m^3 in month is {cost:,.0f} đ.")