
def move_up(row, col):
    return row - 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


def move_down(row, col):
    return row + 1, col


size = int(input())
bunny_row = 0
bunny_col = 0
traps = set()
matrix = []
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        if matrix[row][col] == 'B':
            bunny_row = row
            bunny_col = col

directions = {
    'up': move_up,
    'down': move_down,
    'left': move_left,
    'right': move_right,
}
max_result = float("-inf")
best_steps = []
last_command = ''
for direction, step in directions.items():
    current_row, current_col = bunny_row, bunny_col
    current_result = 0
    current_steps = []
    while True:
        current_row, current_col = step(current_row, current_col)
        if current_row < 0 or current_col < 0 or current_col >= size or current_row >= size:
            break
        if matrix[current_row][current_col] == 'X':
            break
        current_result += int(matrix[current_row][current_col])
        current_steps.append([current_row, current_col])
    if current_result > max_result and current_steps:
        max_result = current_result
        best_steps = current_steps
        last_command = direction

print(last_command)
for i in best_steps:
    print(i)
print(max_result)
