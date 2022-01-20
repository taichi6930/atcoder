import collections
from itertools import accumulate  # 累積和を求めるときに使う


def main():
    n = int(input())
    A = list(map(int, input().split()))
    CurrentLocation = [0]
    MaxLocation = [0]

    for i in range(n):
        cl = CurrentLocation[i]
        ml = MaxLocation[i]

        a = A[i]
        ncl = cl + a
        CurrentLocation.append(ncl)
        MaxLocation.append(max(ml, ncl))

    acc = list(accumulate(CurrentLocation))
    ans = 0

    for i in range(n):
        ans = max(ans, acc[i] + MaxLocation[i + 1])
    print(ans)


if __name__ == '__main__':
    main()
