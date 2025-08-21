# RemovePositions.py
arr = list(map(int, input().split()))
remove_indices = [1, 2, 3, 6]

new_arr = [val for idx, val in enumerate(arr, start=1) if idx not in remove_indices]
print(new_arr)
