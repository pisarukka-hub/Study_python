# find the symmetric difference between two sets
# made by set
N, M = map(int, input().split())
s_1, s_2 = set(), set()
for i in range(N):
    s_1.add(str(input()))
for i in range(M):
    s_2.add(str(input()))
if len(s_1 ^ s_2) > 0:
    print(len(s_1 ^ s_2))
else:
    print("NO")

# made by dictionary
# N, M = map(int, input().split())
# d = {}
# count = 0
# for i in range(N + M):
#     if (name := str(input())) in d:
#         d[name] += 1
#     else:
#         d[name] = 0
# for value in d.values():
#     if value < 1:
#         count += 1
# if count > 1:
#     print(count)
# else:
#     print("Таких нет")