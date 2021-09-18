def main():
    n, k = map(int, input().split())
    S = [int(input()) for _ in range(n)]

    num = 1
    ans = 0

    for i in range(n):
        k = 1
        for j in range(i + 1, n + 1):
            print(S[i: j], j - i)


if __name__ == '__main__':
    main()
