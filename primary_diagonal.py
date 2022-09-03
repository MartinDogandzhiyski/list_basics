n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
diagonal_sum = 0
for row_index in range(n):
    diagonal_sum += matrix[row_index][row_index]
print(diagonal_sum)
