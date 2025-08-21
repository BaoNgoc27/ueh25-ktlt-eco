math = float(input())
phys = float(input())
chem = float(input())

gpa = (math*2 + phys*3 + chem) / 6
if gpa >= 8:
    rating = "Good"
elif gpa >= 6.5:
    rating = "Pretty"
elif gpa >= 5:
    rating = "Average"
else:
    rating = "Weak"

print(f"Average point = {gpa:.2f}, rating {rating}.")