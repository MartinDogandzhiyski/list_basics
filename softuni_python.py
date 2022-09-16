number_of_guests = int(input())
guests = set()
for i in range(number_of_guests):
    guest = input()
    guests.add(guest)
command = input()
while not command == 'END':
    guests.remove(command)
    command = input()
print(len(guests))
for i in sorted(guests):
    print(i)