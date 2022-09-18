first_values = set([int(el) for el in input().split()])
second_values = set([int(el) for el in input().split()])
number = int(input())
for i in range(number):
    command = input().split()
    current_command = command[0] + command[1]
    if current_command == "AddFirst":
        [first_values.add(int(x)) for x in command[2:]]
    elif current_command == 'AddSecond':
        [second_values.add(int(x)) for x in command[2:]]
    elif current_command == 'RemoveFirst':
        first_values = first_values.difference([int(x) for x in command[2:]])
    elif current_command == "RemoveSecond":
        second_values = second_values.difference([int(x) for x in command[2:]])
    else:
        if first_values.issubset(second_values) or second_values.issubset(first_values):
            print("True")
        else:
            print("False")
print(", ".join(str(i) for i in sorted(first_values)))
print(", ".join(str(i) for i in sorted(second_values)))