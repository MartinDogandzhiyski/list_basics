from collections import deque
food = int(input())

orders = deque([int(i) for i in input().split()])
print(max(orders))
while orders:
    if orders[0] <= food:
        food -= orders[0]
        orders.popleft()
    else:
        print(f"Orders left: {' '.join([str(i) for i in orders])}")
        break
if not orders:
    print("Orders complete")
