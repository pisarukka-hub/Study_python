# Process lines and skip comments.
# Interpreter
while (line := str(input())) != "":
    if line[0] == '#':
        continue
    end = line.find("#")
    if end != -1:
        print(line[:end])
    else:
        print(line)