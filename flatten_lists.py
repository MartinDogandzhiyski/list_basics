matrix = []
text = input().split('|')
for i in text:
    current_nums = []
    matrix.append(i.split())
for i in reversed(matrix):
    for n in i:
        print(n, end=" ")
