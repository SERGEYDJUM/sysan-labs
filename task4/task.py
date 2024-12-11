from math import isclose, log2
from itertools import chain
from typing import Iterable
import csv


def entropy(arr: Iterable[float]) -> float:
    return -sum(x * log2(x) for x in arr if not isclose(x, 0))


def load_mat() -> list[list[int]]:
    with open("assets/условная-энтропия-данные.csv", encoding="utf-8") as csv_reader:
        csv_reader = csv.reader(csv_reader)
        _ = next(csv_reader)
        return [[int(x) for x in line[1:]] for line in csv_reader]


def main() -> list[float]:
    M = load_mat()
    m_sum = sum(sum(row) for row in M)
    M = [[el / m_sum for el in row] for row in M]

    E_A = entropy(map(sum, M))
    E_B = entropy(map(sum, map(list, zip(*M))))
    E_AB = entropy(chain(*M))
    E_BifA = E_AB - E_A
    I_AB = E_A + E_B - E_AB

    return [E_AB, E_A, E_B, E_BifA, I_AB]


if __name__ == "__main__":
    print(main())
