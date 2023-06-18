def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        ans += A[i] * 2 ** (n - i - 1)

    print(ans)


if __name__ == '__main__':
    main()
