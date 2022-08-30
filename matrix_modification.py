rows = int(input())
matrix = []
length_of_row = 0
for i in range(rows):
    row = input().split()
    matrix.append([int(x) for x in row])
    length_of_row = len(row)


command = input()
while not command == 'END':
    command_data = command.split()
    current_command = command_data[0]
    row = int(command_data[1])
    col = int(command_data[2])
    val = int(command_data[3])
    if current_command == 'Add':
        if 0 <= row < rows and 0 <= col < length_of_row:
            matrix[row][col] += val
        else:
            print("Invalid coordinates")
    elif current_command == 'Subtract':
        if 0 <= row < rows and 0 <= col < length_of_row:
            matrix[row][col] -= val
        else:
            print("Invalid coordinates")

    command = input()

for i in matrix:
    print(*i, sep=' ')