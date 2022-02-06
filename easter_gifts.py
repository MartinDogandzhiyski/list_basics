gifts_list = input().split()
command = input()
while command != "No Money":
    current_command = command.split()
    current_gift = current_command[1]
    if current_command[0] == "OutOfStock":
        for index in range(len(gifts_list)):
            if gifts_list[index] == current_gift:
                gifts_list[index] = 'None'
    elif current_command[0] == 'Required':
        index = int(current_command[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = current_gift
    elif current_command[0] == 'JustInCase':
        gifts_list[-1] = current_gift
    command = input()
for i in gifts_list:
    if i != 'None':
        print(i, end= " ")