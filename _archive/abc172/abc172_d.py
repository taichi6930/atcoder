import math


def main():  # 約数の個数
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        n = N // i
        ans += 0.5 * n * (2 * i + i * (n - 1))
    print(int(ans))


if __name__ == '__main__':
    main()
