def up(row, col):

    return row - 1, col


def left(row, col):

    return row, col - 1


def right(row, col):

    return row, col + 1


def down(row, col):
    return row + 1, col


presents = int(input())
size = int(input())
matrix = []
santa_row = 0
santa_col = 0
nice_kids = 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        if matrix[row][col] == 'S':
            santa_row = row
            santa_col = col
        elif matrix[row][col] == 'V':
            nice_kids += 1

command = input()
out_of_presents = False
current_kids = 0
matrix[santa_row][santa_col] = '-'
while not command == 'Christmas morning':
    if command == 'up':
        santa_row, santa_col = up(santa_row, santa_col)
    elif command == 'right':
        santa_row, santa_col = right(santa_row, santa_col)
    elif command == 'left':
        santa_row, santa_col = left(santa_row, santa_col)
    elif command == 'down':
        santa_row, santa_col = down(santa_row, santa_col)
    if 0 <= santa_row < size and 0 <= santa_col < size:

        if matrix[santa_row][santa_col] == 'C':
            matrix[santa_row][santa_col] = '-'
            if matrix[santa_row + 1][santa_col] == 'X' and presents:
                matrix[santa_row + 1][santa_col] = '-'
                presents -= 1
            if matrix[santa_row - 1][santa_col] == 'X' and presents:
                matrix[santa_row - 1][santa_col] = '-'
                presents -= 1
            if matrix[santa_row][santa_col - 1] == 'X' and presents:
                matrix[santa_row][santa_col - 1] = '-'
                presents -= 1
            if matrix[santa_row][santa_col + 1] == 'X' and presents:
                matrix[santa_row][santa_col + 1] = '-'
                presents -= 1
            if matrix[santa_row + 1][santa_col] == 'V' and presents:
                matrix[santa_row + 1][santa_col] = '-'
                presents -= 1
                current_kids += 1
            if matrix[santa_row - 1][santa_col] == 'V' and presents:
                matrix[santa_row - 1][santa_col] = '-'
                presents -= 1
                current_kids += 1

            if matrix[santa_row][santa_col - 1] == 'V' and presents:
                matrix[santa_row][santa_col - 1] = '-'
                presents -= 1
                current_kids += 1

            if matrix[santa_row][santa_col + 1] == 'V' and presents:
                matrix[santa_row][santa_col + 1] = '-'
                presents -= 1
                current_kids += 1

        else:
            if matrix[santa_row][santa_col] == 'X':
                matrix[santa_row][santa_col] = '-'
            elif matrix[santa_row][santa_col] == 'V':
                matrix[santa_row][santa_col] = '-'
                current_kids += 1
                presents -= 1
    if current_kids == nice_kids:
        break

    if presents == 0:
        out_of_presents = True
        break
    command = input()

matrix[santa_row][santa_col] = 'S'

if current_kids == nice_kids:
    for row in matrix:
        print(*row, sep=" ")
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
if out_of_presents and current_kids < nice_kids:
    print(f"Santa ran out of presents!")
    for row in matrix:
        print(*row, sep=" ")
    print(f"No presents for {nice_kids - current_kids} nice kid/s.")
