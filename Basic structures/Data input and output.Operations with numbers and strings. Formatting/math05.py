# N - total weight M - total cost K1 - cost of 1st type of product K2 - cost of 2nd type of product
# find cost of each type of product
N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())
x2 = int(N * (M - K1) / (K2 - K1))
x1 = int(N - x2)
print(x1, x2)