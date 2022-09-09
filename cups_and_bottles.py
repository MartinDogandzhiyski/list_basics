from collections import deque
cups_capacity = deque([int(i) for i in input().split()])
filled_bottles = [int(i) for i in input().split()]
wasted_water = 0

while True:
    current_bottle = filled_bottles[-1]
    current_cup = cups_capacity[0]
    if current_bottle < current_cup:
        filled_bottles.pop()
        cups_capacity[0] -= current_bottle
    elif current_bottle == current_cup:
        filled_bottles.pop()
        cups_capacity.popleft()

    else:
        cups_capacity.popleft()
        wasted_water += abs(current_cup - current_bottle)
        filled_bottles.pop()
    if not cups_capacity or not filled_bottles:
        break
if not filled_bottles:
    print(f"Cups: {' '.join([str(i) for i in cups_capacity])}")
    print(f"Wasted litters of water: {wasted_water}")
else:
    print(f"Bottles: {' '.join(map(str, filled_bottles))}")
    print(f"Wasted litters of water: {wasted_water}")