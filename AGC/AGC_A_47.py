import sys
import collections
import bisect
import math
import time


def main():
    n = int(input())
    A = [None] * n
    for i in range(n):
        p = float(input())
        cin = str(p).index(".")
        A[i] = float(str(p)[cin:len(str(p))])
    cnt = 0
    print(A)
    for x in range(n - 1):
        print("x:" + str(x))
        for y in range(1, 10):
            if A[x] == 0:
                cnt += A.count(0)
                break
            k = float(y / A[x])
            print(k)
            cnt += A[x + 1:n].count(k)

    print(cnt)


if __name__ == '__main__':
    main()
