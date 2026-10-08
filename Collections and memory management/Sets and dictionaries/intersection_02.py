# Find the number of common elements in two sets of strings.
#  made by set
N, M = map(int, input().split())
s_1, s_2 = set(), set()
for i in range(N):
    s_1.add(str(input()))
for i in range(M):
    s_2.add(str(input()))
if len(s_1 & s_2) > 0:
    print(len(s_1 & s_2))
else:
    print("NO")

# made by dictionary

# N, M = map(int, input().split())
# d = {}
# count = 0
# for i in range(N):
#     d[str(input())] = 0
# for i in range(M):
#     if (name := str(input())) in d:
#         d[name] += 1
# for value in d.values():
#     if value > 0:
#         count += 1
# if count > 0:
#     print(count)
# else:
#     print("NO")