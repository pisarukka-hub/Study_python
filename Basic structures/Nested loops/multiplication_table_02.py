# show a multiplication table for n numbers
line = ""
for i in range(1,(n := int(input()) + 1)):
    for j in range(1, n):
        line = str(j) + " * " + str(i) + " = " + str(i * j) 
        print(line)
    line = ""