def is_inside(row, col, size=5):
    return 0 <= row < size and 0 <= col < size


def move_up(row, col, steps):
    if is_inside(row - steps, col):
        return row - steps, col


def move_left(row, col, steps):
    if is_inside(row, col - steps):
        return row, col - steps


def move_right(row, col, steps):
    if is_inside(row, col + steps):
        return row, col + steps


def move_down(row, col, steps):
    if is_inside(row + steps, col):
        return row + steps, col

def up(row, col):
    if is_inside(row - 1, col):
        return row - 1, col


def left(row, col):
    if is_inside(row, col - 1):
        return row, col - 1


def right(row, col):
    if is_inside(row, col + 1):
        return row, col + 1


def down(row, col):
    if is_inside(row + 1, col):
        return row + 1, col


matrix = []
my_row = 0
my_col = 0
total_targets = 0

for row in range(5):
    elements = input().split()
    matrix.append(elements)
    for col in range(5):
        if matrix[row][col] == 'A':
            my_row = row
            my_col = col
        elif matrix[row][col] == 'x':
            total_targets += 1

current_targets = total_targets

is_completed = False

all_targets = []

commands = int(input())
for i in range(commands):
    command = input()
    if command:
        command_data = command.split()
        current_command = command_data[0]
        direction = command_data[1]
        current_row, current_col = my_row, my_col
        if current_command == 'move':
            steps = int(command_data[2])
            if direction == 'right':
                if move_right(my_row, my_col, steps):
                    my_row, my_col = move_right(my_row, my_col, steps)
            elif direction == 'left':
                if move_left(my_row, my_col, steps):
                    my_row, my_col = move_left(my_row, my_col, steps)
            elif direction == 'down':
                if move_down(my_row, my_col, steps):
                    my_row, my_col = move_down(my_row, my_col, steps)
            elif direction == 'up':
                if move_up(my_row, my_col, steps):
                    my_row, my_col = move_up(my_row, my_col, steps)
            if matrix[my_row][my_col] == '.':
                continue
            else:
                my_row, my_col = current_row, current_col

        elif current_command == 'shoot':
            current_row, current_col = my_row, my_col
            while True:
                if direction == 'right':
                    if right(current_row, current_col):
                        current_row, current_col = right(current_row, current_col)
                    else:
                        break
                elif direction == 'left':
                    if left(current_row, current_col):
                        current_row, current_col = left(current_row, current_col)
                    else:
                        break
                elif direction == 'down':
                    if down(current_row, current_col):
                        current_row, current_col = down(current_row, current_col)
                    else:
                        break
                elif direction == 'up':
                    if up(current_row, current_col):
                        current_row, current_col = up(current_row, current_col)
                    else:
                        break
                if matrix[current_row][current_col] == 'x':
                    current_targets -= 1
                    matrix[current_row][current_col] = '.'
                    all_targets.append([current_row, current_col])
                    break
    else:
        break

    if current_targets == 0:
        is_completed = True
        break

if is_completed:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {current_targets} targets left.")

for i in all_targets:
    print(i)


