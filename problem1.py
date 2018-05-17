# -*- coding: utf-8 -*-
import sys

infinite = sys.maxsize


def MEMOIZED_MATRIX_CHAIN(p):
    n = len(p) - 1
    m = [[1 for x in range(n + 1)] for x in range(n + 1)]

    for i in range(0, n + 1):
        print(p[i])  # confirm all of elements have been included
        for j in range(i, n + 1):
            m[i][j] = infinite
    return LOOKUP_CHAIN(m, p, 1, n)


def LOOKUP_CHAIN(m, p, i, j):
    if m[i][j] < infinite:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):  # k from i to j-1
            q = LOOKUP_CHAIN(m, p, i, k) + LOOKUP_CHAIN(m, p, k + 1, j) + p[i - 1] * p[k] * p[j]
            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]


def main():
    p = [22, 34, 14, 5, 15, 28, 20, 22, 11, 33, 45]
    print("Number of Multiplications:", MEMOIZED_MATRIX_CHAIN(p))


if __name__ == '__main__':
    main()
