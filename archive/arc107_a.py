import math
mod2 = 998244353


def main():
    a, b, c = map(int, input().split())
    A = (a * (a + 1) // 2) % mod2
    B = (b * (b + 1) // 2) % mod2
    C = (c * (c + 1) // 2) % mod2
    print(A * B * C % mod2)


if __name__ == '__main__':
    main()
