# How many rabbits can you find before we arrive?
m = 0
while (line := str(input())) != "We are coming!":
    if "rabbit" in line:
        m = m + 1
print(m)