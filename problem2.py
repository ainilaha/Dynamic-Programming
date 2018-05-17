# -*- coding: utf-8 -*-
def LCS_LENGTH(X, Y):
    m = len(X)
    n = len(Y)
    b = [[1 for x in range(m + 2)] for x in range(n + 2)]  # one extra for -1 index
    c = [[0 for x in range(m + 2)] for x in range(n + 2)]

    for i in range(0, m):
        c[i][-1] = 0
    for j in range(-1, n):
        c[-1][j] = 0

    for i in range(0, m):
        for j in range(0, n):
            if X[i] == Y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "diag"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "up"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "left"

    return c, b


def PRINT_LCS(b, X, i, j):
    if i == -1 or j == -1:
        return
    if b[i][j] == "diag":
        PRINT_LCS(b, X, i - 1, j - 1)
        print(X[i])
    elif b[i][j] == "up":
        PRINT_LCS(b, X, i - 1, j)
    else:
        PRINT_LCS(b, X, i, j - 1)


def PRTINT_TABLE(c, b, X_len, Y_len, X, Y):
    line_len = 0
    y_line = "yi|     |"
    for y in Y:
        y_line = y_line + y + "      |"
    print(y_line)

    for i in range(-1, X_len):
        line = ""
        for j in range(-1, Y_len):
            if i == -1 or j == -1:
                if j == -1 and i == -1:
                    line = line + "xi|" + str(c[i][j]) + "    |"
                elif j == -1:
                    line = line + X[i] + "|" + str(c[i][j]) + "     |"
                else:
                    line = line + "|" + str(c[i][j]) + "     |"
            else:
                if str(b[i][j]) == "up":
                    line = line + "|" + str(c[i][j]) + " " + str(b[i][j]) + "  |"
                else:
                    line = line + "|" + str(c[i][j]) + " " + str(b[i][j]) + "|"
        if i == -1:
            line_len = len(line)

        print("-" * line_len)
        print(line)
        print("-" * line_len)


def main():
    X = "ABCBDAB"
    Y = "BDCABA"
    c, b = LCS_LENGTH(X, Y)
    PRTINT_TABLE(c, b, len(X), len(Y), X, Y)
    print('Length of LSC is', c[len(X) - 1][len(Y) - 1], "\nCommon Elements Are:")
    PRINT_LCS(b, X, len(X) - 1, len(Y) - 1)


if __name__ == '__main__':
    main()
