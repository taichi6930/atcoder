def main():
    n = int(input())
    A = list(map(int, input().split()))
    AMax = [A[0]] * n
    B = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        AMax[i] = max(AMax[max(i - 1, 0)], A[i])
        ans = max(ans, AMax[i] * B[i])
        print(ans)


if __name__ == '__main__':
    main()
