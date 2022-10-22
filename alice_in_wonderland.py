
def move_up(row, col):
    return row - 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


def move_down(row, col):
    return row + 1, col


size = int(input())
alice_row = 0
alice_col = 0
rabbit_row = 0
rabbit_col = 0
matrix = []
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        if matrix[row][col] == 'A':
            alice_row = row
            alice_col = col
        elif matrix[row][col] == 'R':
            rabbit_row = row
            rabbit_col = col
matrix[alice_row][alice_col] = '*'
tea_quantity = 0
is_collected = False
while True:
    command = input()
    if command == 'down':
        alice_row, alice_col = move_down(alice_row, alice_col)
    if command == 'right':
        alice_row, alice_col = move_right(alice_row, alice_col)
    if command == 'left':
        alice_row, alice_col = move_left(alice_row, alice_col)
    if command == 'up':
        alice_row, alice_col = move_up(alice_row, alice_col)

    if alice_row < 0 or alice_col < 0 or alice_col >= size or alice_row >= size:
        break
    if matrix[alice_row][alice_col] == 'R':
        matrix[alice_row][alice_col] = '*'
        break
    if matrix[alice_row][alice_col] == '.':
        matrix[alice_row][alice_col] = '*'
        continue
    if matrix[alice_row][alice_col] == '*':
        continue
    tea_quantity += int(matrix[alice_row][alice_col])
    matrix[alice_row][alice_col] = '*'
    if tea_quantity >= 10:
        is_collected = True
        break

if not is_collected:
    print(f"Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for rows in matrix:
    print(*rows, sep=" ")
