import numpy as np

def count_straight(mat: np.array):
    count = 0
    for row in mat:
        for i, c in enumerate(row):
            if (
                len(row) - i >= 4
                and "".join(row[i:i+4]) == "XMAS"
            ):
                count += 1
            if (
                0 + i >= 3
                and "".join(row[i-3:i+1]) == "SAMX"
            ):
                count += 1
    return count


def count_diag(mat: np.array):
    count = 0
    for j, row in enumerate(mat):
        for i, c in enumerate(row):
            if (
                len(mat) - j >= 4
                and len(row) - i >= 4
            ):
                line = "".join([mat[j][i], mat[j+1][i+1], mat[j+2][i+2], mat[j+3][i+3]])

                if (
                    line == "XMAS"
                    or line == "SAMX"

                ):
                    count += 1
            if (
                len(mat) - j >= 4
                and 0 + i >= 3
            ):
                line = "".join([mat[j][i], mat[j+1][i-1], mat[j+2][i-2], mat[j+3][i-3]])
                if (
                    line == "XMAS"
                    or line == "SAMX"
                ):
                    count += 1

    return count


with open("./input.txt") as file:
    mat = np.array([[c for c in line.strip()] for line in file.readlines()])

    count_horizontal = count_straight(mat)
    count_vertical = count_straight(mat.T)
    count_diag = count_diag(mat)
    count = count_horizontal + count_vertical + count_diag

    print(f"horizontal: {count_horizontal}\nvertical: {count_vertical}\ndiagonal: {count_diag}\ntotal: {count}")
