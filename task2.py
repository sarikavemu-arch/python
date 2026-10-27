days = int(input("Enter required validity days: "))

plans = [
    ["Plan A", 199, 2, 28],
    ["Plan B", 299, 3, 56],
    ["Plan C", 399, 5, 84]
]

best_cost = 99999
best_plan = "No eligible plan"

for plan in plans:
    name = plan[0]
    price = plan[1]
    data = plan[2]
    validity = plan[3]

    extra = 0
    if usage > data:
        extra = (usage - data) * 20

    total = price + extra

    if validity >= days and total <= budget:
        if total < best_cost:
            best_cost = total
            best_plan = name

print("Best Plan:", best_plan)

if best_plan != "No eligible plan":
    print("Total Cost:", best_cost)
else:
    print("No plan fits your budget and validity")
