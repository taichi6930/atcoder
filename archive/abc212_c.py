from bisect import bisect_left


def main():
    n, m = map(int, input().split())
    [A, B] = [sorted(list(map(int, input().split()))) for _ in range(2)]

    ans = 10 ** 10

    for i in range(n):
        q = bisect_left(B, A[i])
        ans = min(abs(A[i] - B[max(0, q - 1)]), abs(A[i] -
                                                    B[min(m - 1, q)]), abs(A[i] - B[min(m - 1, q + 1)]), ans)
    print(ans)


if __name__ == '__main__':
    main()
