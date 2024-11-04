import json


def load_mat(path: str) -> list[list[bool]]:
    with open(path, encoding="utf-8") as json_file:
        data = json.load(json_file)
        elements = []

        for element in data:
            if isinstance(element, int):
                elements.append(element)
            else:
                elements.extend(element)

        mat = [[True for _ in range(len(elements))] for _ in range(len(elements))]

        for element in data:
            if isinstance(element, int):
                i = elements.index(element)
                for j in elements[:i]:
                    mat[j - 1][element - 1] = False
            else:
                imn = elements.index(min(element))
                imx = elements.index(max(element))

                for k in elements[imn : imx + 1]:
                    for j in elements[:imn]:
                        mat[j - 1][k - 1] = False

        return mat


def mat_logmul(A, B):
    C = A
    for i in range(len(B)):
        for j in range(len(B[0])):
            C[i][j] = C[i][j] and B[i][j]
    return C


def mat_tlogadd(A):
    C = A
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] or A[j][i]
    return C


if __name__ == "__main__":
    A = load_mat("assets/task5_1.json")
    B = load_mat("assets/task5_2.json")

    C = mat_logmul(A, B)
    D = mat_tlogadd(C)

    conflicts = set()
    for i, row in enumerate(D):
        if False in row:
            j = row.index(False)
            if (j, i) not in conflicts:
                conflicts.add((i, j))

    print(json.dumps([[c[0]+1, c[1]+1] for c in conflicts]))