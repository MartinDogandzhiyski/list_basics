clothes = [int(i) for i in input().split()]
capacity_of_rack = int(input())
racks = 0
sum_of_clothes = 0
while clothes:
    sum_of_clothes += clothes[-1]
    if sum_of_clothes < capacity_of_rack:
        clothes.pop()
        if len(clothes) == 0:
            racks += 1
    elif sum_of_clothes == capacity_of_rack:
        clothes.pop()
        sum_of_clothes = 0
        racks += 1
    else:
        sum_of_clothes = 0
        racks += 1
print(racks)
