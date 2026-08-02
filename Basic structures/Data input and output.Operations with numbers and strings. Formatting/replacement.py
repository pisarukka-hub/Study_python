# abcd to badc
inp = int(input())
a = str(inp // 1000)
b = str((inp % 1000) // 100)
c = str((inp % 100) // 10) 
d = str(inp % 10)
print(b + a + d + c)