

events_list = input().split("|")
max_energy = 100
coins = 100
current_event = []
not_managed_to_finish_orders = False
current_energy = 0
gained_energy = 0
for event in events_list:
    current_event = event.split("-")
    event_name = current_event[0]
    value = int(current_event[-1])
    if event_name == "rest":
        current_energy = max_energy
        max_energy += value
        gained_energy += value

        if max_energy > 100:
            max_energy = 100
            gained_energy = 100 - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {max_energy}.")
    elif event_name == "order":
        max_energy -= 30
        if max_energy >= 0:
            coins += value
            print(f"You earned {value} coins.")
        else:
            max_energy += 80
            print("You had to rest!")
            continue
    else:
        if coins > value:
            coins -= value
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            not_managed_to_finish_orders = True
            break

if not_managed_to_finish_orders:
    pass
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {max_energy}")
