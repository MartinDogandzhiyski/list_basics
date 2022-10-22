parentheses = input()
opening_brackets = []
balanced = True
for i in parentheses:
    if i in '({[':
        opening_brackets.append(i)
    else:
        if opening_brackets:
            last_opening_bracket = opening_brackets.pop()
            if f"{last_opening_bracket}{i}" not in '()[]{}':
                balanced = False
                break
        else:
            balanced = False
            break
if balanced and not opening_brackets:
    print(f"YES")
else:
    print("NO")
