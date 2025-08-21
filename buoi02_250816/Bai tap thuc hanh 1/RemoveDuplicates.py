# RemoveDuplicates.py
arr = list(map(int, input().split()))
res = []
for x in arr:
    if x not in res:
        res.append(x)
print(res)