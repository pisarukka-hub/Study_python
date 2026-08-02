name = str(input())
cost = int(input())
weight = int(input())
money = int(input())
bill = "receipt"
coststr = str(weight) + "kg * " + str(cost) + "USD/kg"
total = cost * weight
change = money - total
print(f"{bill:=^35}")
print(f"Product:{name: >27}")
print(f"Price:{coststr: >29}")
print(f"Total:{total: >26}USD")
print(f"Paid:{money: >27}USD")
print(f"Change:{change: >25}USD")
print("=" * 35)