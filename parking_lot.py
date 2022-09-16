n = int(input())
plates = set()
for i in range(n):
    command, number_plate = input().split(', ')
    if command == "IN":
        plates.add(number_plate)
    elif command == 'OUT':
        plates.remove(number_plate)
if plates:
    print('\n'.join(plates))
else:
    print("Parking Lot is Empty")