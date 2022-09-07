n = int(input())
matrix = []
for i in range(n):
    matrix.append(input())
symboll = input()
is_occur = False
for r in range(n):
    if is_occur:
        break
    for c in range(len(matrix[r])):
        if matrix[r][c] == symboll:
            print(f"{r, c}")
            is_occur = True
            break
if not is_occur:
    print(f"{symboll} does not occur in the matrix")