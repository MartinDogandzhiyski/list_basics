list_of_numbers = input().split()
count_of_numbers_to_remove = int(input())
numbers_as_int = []
for i in list_of_numbers:
    numbers_as_int.append(int(i))
for _ in range(count_of_numbers_to_remove):
    numbers_as_int.remove(min(numbers_as_int))
print(*numbers_as_int, sep=", ")

