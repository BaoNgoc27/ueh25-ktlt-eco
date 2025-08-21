# CountOccurrences.py
arr = list(map(int, input().split()))
res = []
for x in arr:
    if x not in [r[0] for r in res]:
        cnt = 0
        for y in arr:
            if x == y:
                cnt += 1
        res.append((x, cnt))

for val, cnt in res:
    print(f"{val}: {cnt}")