from bisect import bisect_left
from itertools import accumulate


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] + list(accumulate(A))
    ans = 0

    for b in B:
        i = bisect_left(B, b + k)
        if i == n + 1:
            break
        ans += n + 1 - i
    print(ans)


if __name__ == '__main__':
    main()
