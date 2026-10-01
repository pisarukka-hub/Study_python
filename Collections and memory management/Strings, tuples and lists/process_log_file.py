# Process a log file by removing ## from the beginning of lines
# and deleting lines that end with @@@.

while (line := str(input())) != "":
    if line[:2] == "##": 
        line = line[2:]
    if line[-3:] == "@@@":
        continue
    print(line)