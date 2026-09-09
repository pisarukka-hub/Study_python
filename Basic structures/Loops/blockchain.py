# Check if the hash of a block is valid
answer = -1
oldhash = 0
for N in range(int(input())):
    block = int(input())
    info = block // (256**2)
    block = block - (info * (256**2))
    random = block // 256
    block = block - (random * 256)
    hash = block
    if (hash != (((info + random + oldhash) * 37)) % 256):
        answer = N
        break
    if (hash >= 100):
        answer = N
        break
    oldhash = hash
print(answer)