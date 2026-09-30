# Calculate the total price of items with a 10% discount on items costing 500 or more
s = 0.
while a := float(input()):
    if a >= 500:
        a *= 0.9
    s += a
print(s) 