name = str(input())
cost = int(input())
weight = int(input())
money = int(input())
total = cost * weight
change = money - total
print("receipt")
print(name, " - ", weight, "kg - ", cost, "USD/kg", sep="")
print("Total: ", total, "USD\n", "Amount inserted: ", money, "USD\n", "Change: ", change, "USD", sep="")