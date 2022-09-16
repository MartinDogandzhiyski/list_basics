numbers = (float(el) for el in input().split())
occ = {}
for num in numbers:
    if num not in occ:
        occ[num] = 1
    else:
        occ[num] += 1
for key, val in occ.items():
    print(f"{key} - {val} times")