def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    allGet = k // n
    amari = k - allGet * n
    B = sorted(A)[amari]
    for i in range(n):
        ans = allGet + (1 if B > A[i] else 0)
        print(ans)


if __name__ == '__main__':
    main()
