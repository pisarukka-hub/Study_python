# kid's garden cards 
# cabinet number is a three-digit number, where the first digit is the group number, the second digit is the bed number, and the third digit is the ID number of the child in the group.
name = str(input())
totalnum = int(input())
groupnum = totalnum // 100
bednum = (totalnum - (groupnum * 100)) // 10
idnum = totalnum % 10
print("Group №", groupnum, ".", sep="")
print(idnum, ". ", name, ".", sep="")  
print("Cabinet: ", totalnum, ".\n", "Bed: ", bednum, ".", sep="")
