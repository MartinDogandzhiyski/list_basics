from collections import deque
chocolates = [int(x) for x in input().split(", ")]
cups_milk = deque([int(x) for x in input().split(", ")])
milkshakes = 0
milkshakes_done = False
while chocolates and cups_milk:
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cups_milk[0] <= 0:
        cups_milk.popleft()
        continue
    if chocolates[-1] == cups_milk[0]:
        milkshakes += 1
        chocolates.pop()
        cups_milk.popleft()
    else:
        chocolates[-1] -= 5
        cups_milk.append(cups_milk.popleft())
    if milkshakes == 5:
        milkshakes_done = True
        break

if milkshakes_done:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")
if cups_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_milk)}")
else:
    print("Milk: empty")