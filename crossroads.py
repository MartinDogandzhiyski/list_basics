
from collections import deque
green_light = int(input())
free_window = int(input())
cars = deque()
cars_passed = 0
command = input()
while not command == 'END':
    cars.append(command)
    command = input()
cars.append('END')
current_green_light = green_light
safe = True
current_car = ''
while cars:
    if cars[0] == 'END':
        cars.popleft()
    if cars[0] == 'green':
        if cars[1] == 'END':
            cars.popleft()
            break
        else:
            if
            cars.popleft()
            current_green_light = green_light
        continue
    if current_green_light > 0 and free_window + current_green_light < len(cars[0]):
        print(f"A crash happened!")
        print(f"{cars[0]} was hit at {cars[0][free_window + current_green_light]}.")
        safe = False
        break
    elif current_green_light <= 0:

        current_car = cars.popleft()
        continue
    elif current_green_light > 0 and free_window + current_green_light >= len(cars[0]):
        cars_passed += 1
        current_green_light -= len(cars[0])
        cars.popleft()

if safe:
    print(f"Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
