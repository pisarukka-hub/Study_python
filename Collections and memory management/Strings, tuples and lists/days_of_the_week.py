# show n days in given order (for example days of the week)
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for i in range(int(input())):
    print(order[i % len(order)])