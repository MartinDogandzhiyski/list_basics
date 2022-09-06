n, m = [int(x) for x in input().split(', ')]
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split(', ')])
sums = []
squares = []
max_val = 0
for r in range(n - 1):
    for c in range(m - 1):
        current_sum =  matrix[r][c] + \
            matrix[r][c + 1] + \
            matrix[r + 1][c] + \
            matrix[r + 1][c + 1]
        sums.append((
            current_sum,
            r,
            c
        ))
index = 0
for i in range(len(sums)):
    if sums[i][0] > max_val:
        max_val = sums[i][0]
        index = i
print(f"{matrix[sums[index][1]][sums[index][2]]} {matrix[sums[index][1]][sums[index][2] + 1]}")
print(f"{matrix[sums[index][1] + 1][sums[index][2]]} {matrix[sums[index][1] + 1][sums[index][2] + 1]}")
print(max_val)
