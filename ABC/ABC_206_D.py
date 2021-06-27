import math
import collections


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = []

    for i in range(n):
        if A[i] != A[n - i - 1]:
            B.append(A[i])
            B.append(A[n - i - 1])
    if len(B) == 0:
        print(0)
        return
    print(len(set(B)) - 1)


if __name__ == '__main__':
    main()
