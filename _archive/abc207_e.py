mod = 10 ** 9 + 7


def main():
    n = int(input())
    A = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        B = A[i + 1:n]
        if len(B) == 0:
            ans = (ans + 1) % mod
        print(B)
        for j in range(i + 1, n):
            pass


if __name__ == '__main__':
    main()
