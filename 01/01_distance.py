from util import load_columns

l1, l2 = load_columns("./input.txt")
l1.sort()
l2.sort()

distances = []
for l, r in zip(l1, l2):
    distances.append(abs(l - r))

print(sum(distances))
