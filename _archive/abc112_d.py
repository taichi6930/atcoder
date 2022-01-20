import math


def main():
    n, m = map(int, input().split())
    ans = 1
    for i in range(1, m):
        j = m - (n - 1) * i
        if j <= 0 or i > j:
            break
        ans = max(ans, math.gcd(i, j))
    print(ans)


if __name__ == '__main__':
    main()
