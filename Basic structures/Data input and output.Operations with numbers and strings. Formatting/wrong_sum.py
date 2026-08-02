# sum without carrying
inp1 = int(input())
inp2 = int(input())
a1 = int(inp1 // 100)
b1 = int((inp1 % 100) // 10)
c1 = int(inp1 % 10)
a2 = int(inp2 // 100)
b2 = int((inp2 % 100) // 10) 
c2 = int(inp2 % 10)
a3 = (a1 + a2) % 10
b3 = (b1 + b2) % 10
c3 = (c1 + c2) % 10
answ = (a3 * 100) + (b3 * 10) + c3
print(answ)