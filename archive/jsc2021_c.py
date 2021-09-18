import math


def main():
    a, b = map(int, input().split())
    ans = 1

    for i in range(1, a + 1):
        if math.floor(b / i) * i <= math.ceil(a / i) * i:
            continue
        ans = i
    print(ans)


if __name__ == '__main__':
    main()
