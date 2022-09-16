number_of_students = int(input())
grades_dict = {}
for i in range(number_of_students):
    student, grade = input().split()
    if student not in grades_dict:
        grades_dict[student] = [float(grade)]
    else:
        grades_dict[student].append(float(grade))
for key, val in grades_dict.items():
    print(f"{key} -> {' '.join(f'{el:.2f}' for el in val)} (avg: {sum(val) / len(val):.2f})")