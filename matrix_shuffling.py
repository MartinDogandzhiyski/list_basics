rows, cols = [int(x) for x in input().split()]
matrix = []
for i in range(rows):
    matrix.append(input().split())

command = input()
while not command == 'END':
    command_data = command.split()
    current_command = command_data[0]
    if current_command == 'swap':
        if len(command_data) == 5:
            row_1 = int(command_data[1])
            col_1 = int(command_data[2])
            row_2 = int(command_data[3])
            col_2 = int(command_data[4])
            if 0 <= rows < row_1 and 0 <= rows < row_2 and 0 <= cols < col_1 and 0 <= cols < col_2:
                print("Invalid input!")

            else:
                first_char = matrix[row_1][col_1]
                matrix[row_1][col_1] = matrix[row_2][col_2]
                matrix[row_2][col_2] = first_char
                for row in range(rows):
                    for col in range(cols):
                        print(f"{matrix[row][col]}", end=' ')
                    print()
        else:
            print('Invalid input!')

    else:
        print("Invalid input!")

    command = input()