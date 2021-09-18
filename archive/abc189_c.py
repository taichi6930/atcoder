import math
from itertools import accumulate


def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        k = A[i]
        for j in range(i, n):
            k = min(A[j], k)
            ans = max(k * (j - i + 1), ans)
    print(ans)


if __name__ == '__main__':
    main()
