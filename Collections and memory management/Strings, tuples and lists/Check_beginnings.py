# If a string starts with a, b, or c, print "Yes". Otherwise, print "No".
for i in range(int(input())):
    if str(input())[0] not in 'abc':
        print("No")
        break
else: print("Yes")