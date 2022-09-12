from collections import deque
price_of_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = [int(i) for i in input().split()]
locks = deque([int(i) for i in input().split()])
value_of_intelligence = int(input())
counter = 0
total_bullets = 0
total_locks = 0
while True:
    current_bullet = bullets[-1]
    current_lock = locks[0]
    if counter == size_of_gun_barrel:
        print("Reloading!")
        counter = 0
    if current_bullet <= current_lock:
        print("Bang!")
        bullets.pop()
        locks.popleft()
        total_locks += 1
        total_bullets += 1
    else:
        total_bullets += 1
        print("Ping!")
        bullets.pop()
    counter += 1
    if not bullets or not locks:
        if counter == size_of_gun_barrel and len(bullets) > 0:
            print("Reloading!")
        break

if not bullets and not locks:
    print(f"0 bullets left. Earned ${value_of_intelligence - total_bullets * price_of_bullet}")
elif not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence - total_bullets * price_of_bullet}")