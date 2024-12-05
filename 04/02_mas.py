import numpy as np

def count_x_mas(mat: np.array):
    count = 0
    for j, row in enumerate(mat):
        for i, c in enumerate(row):
            if (
                len(mat) - j >= 3
                and len(row) - i >= 3
            ):
                down = "".join([mat[j][i], mat[j+1][i+1], mat[j+2][i+2]])
                up = "".join([mat[j+2][i], mat[j+1][i+1], mat[j][i+2]])
                if (
                    (down == "MAS" or down == "SAM")
                    and (up == "MAS" or up == "SAM")
                ):
                    print(np.array([
                        mat[j][i:i+3],
                        mat[j+1][i:i+3],
                        mat[j+2][i:i+3],
                    ]))
                    print(down)
                    print(up)
                    count += 1

    return count


with open("./input.txt") as file:
    mat = np.array([[c for c in line.strip()] for line in file.readlines()])
    print(count_x_mas(mat))
