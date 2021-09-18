import math


def main():
    n, m = map(int, input().split())
    A = []
    B = []
    for i in range(m):
        ab = sorted(list(map(int, input().split())))
        if ab[0] == 1:
            A.append(ab[1])
            continue
        if ab[1] == n:
            B.append(ab[0])
    setA = set(A)
    setB = set(B)
    setAB = set(A + B)
    print("POSSIBLE" if len(setA) + len(setB) != len(setAB) else "IMPOSSIBLE")


if __name__ == '__main__':
    main()
