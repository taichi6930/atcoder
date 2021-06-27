import collections
import math


def main():
    A = []
    n, p = map(int, input().split())
    q = 2
    for i in range(p + 1):
        if p == 1:
            break
        if p % q == 0:
            A.append(q)
            p = p // q
            continue
        q += 1
    C = collections.Counter(A)
    if len(A) < n:
        print(1)
        return

    ans = 1
    for j in range(len(C.keys())):
        a = C.most_common()[j][0]
        b = C.most_common()[j][1]
        if b < n:
            break
        ans *= a ** (b // n)

    print(ans)


if __name__ == '__main__':
    main()
