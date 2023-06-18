import math


def main():
    a1, a2, a3 = map(int, input().split())
    p = 2 * a2 - a1 - a3

    ans = 0

    if p < 0:
        if p % 2 == 0:
            ans += math.ceil(p // (-2))
        elif p % 2 != 0:
            p -= 1
            ans += 1
            ans += math.ceil(p // (-2))
    elif p > 0:
        ans = p

    print(ans)


if __name__ == '__main__':
    main()
