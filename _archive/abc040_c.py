def main():
    n = int(input())
    A = list(map(int, input().split()))
    DP = [0] + [abs(A[1] - A[0])] + [None] * (n - 2)
    for i in range(n - 2):
        DP[i + 2] = min(DP[i] + abs(A[i + 2] - A[i]),
                        DP[i + 1] + abs(A[i + 2] - A[i + 1]))
    print(DP[-1])


if __name__ == '__main__':
    main()
