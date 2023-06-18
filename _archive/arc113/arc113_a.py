import math


def main():
    k = int(input())
    ans = 0
    for a in range(1, k + 1):
        for b in range(1, k + 1):
            c = math.floor(k / a / b)
            if c <= 0:
                break
            ans += c
    print(ans)


if __name__ == '__main__':
    main()
