n, m = [int(x) for x in input().split(', ')]
matrix = []
for i in range(n):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)
col_sum = 0
time = 0
for column_index in range(m):
    col_sum = 0
    for row_index in range(n):
        row = matrix[row_index]
        col_sum += row[column_index]
    print(col_sum)