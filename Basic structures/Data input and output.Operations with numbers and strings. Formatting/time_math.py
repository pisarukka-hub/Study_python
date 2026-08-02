# what time will it be after a certain number of minutes?
hournow = int(input())
minutnow = int(input())
time = int(input())
allminut = (hournow * 60) + minutnow + time
hourafter = (allminut // 60) % 24
minutafter = allminut % 60
firsth = hourafter // 10
sech = hourafter % 10
firstm = minutafter // 10
secm = minutafter % 10
print(firsth, sech, ":", firstm, secm, sep="")