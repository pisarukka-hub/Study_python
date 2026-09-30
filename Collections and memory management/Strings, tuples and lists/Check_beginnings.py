#If str starts with a or b or c print Yes. Else print No
for i in range(int(input())):
    if str(input())[0] not in 'abc':
        print("No")
        break
else: print("Yes")