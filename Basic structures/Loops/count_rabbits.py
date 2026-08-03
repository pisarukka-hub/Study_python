# How many rabbits can you find outside while we are coming?
m = 0
while (line := str(input())) != "We are coming!":
    if "rabbit" in line:
        m = m + 1
print(m)