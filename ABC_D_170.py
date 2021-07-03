import sys
import collections
import bisect


def main():
    n = int(input())
    A = sorted(list(map(int, input().split())))
    c = collections.Counter(A)
    cKeys, cLen = sorted(c.keys()), len(c)
    sumA = 0
    print(cKeys)
    if cLen == 1:
        print(0)
        return
    for num in range(2, len(cLen) + 1):
        if cKeys[num] != 1:
            continue
        for j in range(num):
            if cKeys[num] < cKeys[j] * 2:
                continue

    print(sumA)


if __name__ == '__main__':
    main()
