stack = []
n = int(input())
for i in range(n):
    command = input().split()
    current_command = command[0]
    if current_command == '1':
        stack.append(int(command[1]))
    elif current_command == '2':
        if stack:
            stack.pop()
    elif current_command == '3':
        if stack:
            print(max(stack))
    elif current_command == '4':
        if stack:
            print(min(stack))
print(*stack[::-1], sep=', ')

