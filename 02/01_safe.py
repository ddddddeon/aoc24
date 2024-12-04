from util import is_safe
   
with open("./input.txt") as file:
    num_safe = 0
    for line in file.readlines():
        numbers = [int(num) for num in line.split()]
        if is_safe(numbers):
            num_safe += 1

    print(num_safe)


