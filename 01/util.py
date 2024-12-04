def load_columns(filename: str) -> tuple[list[int], list[int]]:
    l1 = []
    l2 = []

    with open(filename) as file:
        for line in file.readlines():
            left, right = line.split()
            l1.append(int(left))
            l2.append(int(right))

    return (l1, l2)
