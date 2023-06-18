import math


def main():
    n = int(input())
    bMax = int(math.log(n, 2))
    ans = 10 ** 18
    for b in range(bMax + 1):
        a = int(n // (2 ** b))
        c = n - a * 2 ** b
        if a < 0 or b < 0 or c < 0:
            continue
        ans = min(a + b + c, ans)

    print(ans)


if __name__ == '__main__':
    main()
