import re

with open("./input.txt") as file:
    total = 0
    contents = file.read()
    contents = contents.split("do")

    for chunk in contents:
        if not chunk.startswith("n't"):
            for match in re.finditer(r"mul\((\d+)\,(\d+)\)", chunk):
                total += (int(match.group(1)) * int(match.group(2)))

    print(total)
