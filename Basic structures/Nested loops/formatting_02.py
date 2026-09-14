# Show time to start for n racers
for i in range(1, (n := int(input())) + 1):
    k = i + 2
    for j in range(k):
        print("Time to start " + str(k) + " seconds")
        k -= 1
    print("Start " + str(i) + "!!!")