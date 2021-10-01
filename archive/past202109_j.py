from bisect import *
import collections


def main():
    n, q = map(int, input().split())
    P = []
    swi = 0
    for i in range(q):
        t, k = map(int, input().split())

        if t == 1:
            if swi == 1:
                P.sort()
                swi = 0
            x = bisect_right(P, k)
            y = 0
            if k > n:
                y = bisect_left(P, 2 * n - k - 1)
            if(x + y) % 2 == 0:
                print(k)
            if (x + y) % 2 == 1:
                print(2 * n - k + 1)
        if t == 2:
            swi = 1
            P.append(n - k + 1)


if __name__ == '__main__':
    main()
