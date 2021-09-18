import math


def main():
    s = list(input())
    n = len(s)
    L, R = [0] * (n + 1), [0] * (n + 1)
    for i in range(n):
        L[i + 1] = L[i]
        R[i + 1] = R[i]
        if s[i] == "L":
            L[i + 1] += 1
        else:
            R[i + 1] += 1
    print(L, R)


if __name__ == '__main__':
    main()
