def main():
    n, k = map(int, input().split())
    T = [int(input()) for _ in range(n)]
    S = [None for _ in range(n - 2)]
    S[0] = sum(T[0: 3])
    if S[0] < k:
        print(3)
        return
    for i in range(n - 3):
        S[i + 1] = S[0] - T[i] + T[i + 3]
        if S[i + 1] < k:
            print(i + 4)
            return
    print(-1)


if __name__ == '__main__':
    main()
