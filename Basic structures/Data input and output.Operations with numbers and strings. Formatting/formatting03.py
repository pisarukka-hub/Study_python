name = str(input())
cost = int(input())
weight = int(input())
money = int(input())
bill = "receipt"
coststr = str(weight) + "kg * " + str(cost) + "USD/kg"
total = cost * weight
change = money - total
print(f"{bill:=^35}")
print(f"product:{name:>29}")
print(f"Price:{coststr:>30}")
print(f"Total:{total:>26}USD")
print(f"Paid:{money:>24}USD")
print(f"Change:{change:>26}USD")
print("=" * 35)