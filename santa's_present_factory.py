from collections import deque
materials_for_toys = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
toys_dict = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}
while magic_level and materials_for_toys:
    result = 0
    if magic_level[0] * materials_for_toys[-1] == 150:
        toys_dict["Doll"] += 1
        magic_level.popleft()
        materials_for_toys.pop()
    elif magic_level[0] * materials_for_toys[-1] == 250:
        toys_dict["Wooden train"] += 1
        magic_level.popleft()
        materials_for_toys.pop()
    elif magic_level[0] * materials_for_toys[-1] == 300:
        toys_dict["Teddy bear"] += 1
        magic_level.popleft()
        materials_for_toys.pop()
    elif magic_level[0] * materials_for_toys[-1] == 400:
        toys_dict["Bicycle"] += 1
        magic_level.popleft()
        materials_for_toys.pop()
    elif magic_level[0] * materials_for_toys[-1] < 0:
        result = magic_level[0] + materials_for_toys[-1]
        magic_level.popleft()
        materials_for_toys.pop()
        materials_for_toys.append(result)
    elif magic_level[0] * materials_for_toys[-1] == 0:
        if magic_level[0] == 0 and materials_for_toys == 0:
            magic_level.popleft()
            materials_for_toys.pop()
        elif magic_level[0] == 0:
            magic_level.popleft()
        elif materials_for_toys[-1] == 0:
            materials_for_toys.pop()
        continue
    else:
        magic_level.popleft()
        materials_for_toys[-1] += 15


sorted_dict = {k: v for k, v in sorted(toys_dict.items())}


if toys_dict["Teddy bear"] > 0 and toys_dict["Bicycle"] > 0:
    print("The presents are crafted! Merry Christmas!")
    if materials_for_toys:
        print(f"Materials left: {', '.join(str(x) for x in reversed(materials_for_toys))}")
    if magic_level:
        print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
    for key, val in sorted_dict.items():
        if val > 0:
            print(f"{key}: {val}")
elif toys_dict["Doll"] > 0 and toys_dict["Wooden train"] > 0:
    print("The presents are crafted! Merry Christmas!")
    if materials_for_toys:
        print(f"Materials left: {', '.join(str(x) for x in reversed(materials_for_toys))}")
    if magic_level:
        print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
    for key, val in sorted_dict.items():
        if val > 0:
            print(f"{key}: {val}")
else:
    print("No presents this Christmas!")

    if materials_for_toys:
        print(f"Materials left: {', '.join(str(x) for x in reversed(materials_for_toys))}")
    if magic_level:
        print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
    for key, val in sorted_dict.items():
        if val > 0:
            print(f"{key}: {val}")