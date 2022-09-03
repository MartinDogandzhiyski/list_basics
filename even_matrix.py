rows = int(input())
matrix = []
for i in range(rows):
    even_nums = [int(x) for x in input().split(', ')]
    matrix.append(even_nums)
even_matrix = []
for row in matrix:
    only_even = [x for x in row if x % 2 == 0]
    even_matrix.append(only_even)
print(even_matrix)