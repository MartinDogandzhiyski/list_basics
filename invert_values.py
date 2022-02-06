list_of_nums = input().split(" ")
new_list = []
number = 0
for index in range(len(list_of_nums)):
    number += -1 * (int(list_of_nums[index]))
    new_list.append(number)
    number = 0
print(new_list)
