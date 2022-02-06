items = input().split("|")
budget = float(input())
starting_budget = budget
go_to_france = False
profit = 0
new_prices = []
total_price = 0
for curr in items:
    current_item = curr.split("->")
    type = current_item[0]
    price = float(current_item[1])
    if type == "Clothes":
        if price > 50:
            continue
    elif type == "Shoes":
        if price > 35:
            continue
    elif type == "Accessories":
        if price > 20.50:
            continue
    if budget < price:
        continue
    new_prices.append(float(price * 1.4))
    budget -= price
    profit += price * 0.4
    total_price += price * 1.4
    if budget + total_price >= 150:
        go_to_france = True
        continue
list_for_print = ["%.2f" % elem for elem in new_prices]
print(" ".join(list_for_print))
print(f"Profit: {profit:.2f}")
if go_to_france:
    print("Hello, France!")
else:
    print("Not enough money.")