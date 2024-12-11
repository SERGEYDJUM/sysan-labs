from collections import defaultdict
from math import isclose, log2


def arr_entropy(arr: list[float]) -> float:
    return -sum(x * log2(x) for x in arr if not isclose(x, 0))


def main() -> list[float]:
    dice_probs = dict([(x, 1 / 6) for x in range(1, 7)])

    A_probs = defaultdict(float)
    B_probs = defaultdict(float)
    AB_probs = defaultdict(float)

    for x, px in dice_probs.items():
        for y, py in dice_probs.items():
            xy_p = px * py
            A_probs[x + y] += xy_p
            B_probs[x * y] += xy_p
            AB_probs[(x + y, x * y)] += xy_p

    E_A = arr_entropy(A_probs.values())
    E_B = arr_entropy(B_probs.values())
    E_AB = arr_entropy(AB_probs.values())
    E_BifA = E_AB - E_A
    I_AB = E_A + E_B - E_AB

    return [E_AB, E_A, E_B, E_BifA, I_AB]


if __name__ == "__main__":
    print(main())
