import re

with open("./input.txt") as file:
    total = 0
    contents = file.read()
    for match in re.finditer(r"mul\((\d+)\,(\d+)\)", contents):
        total += (int(match.group(1)) * int(match.group(2)))

    print(total)
