def main():
    ans = 1
    n, m = map(int, input().split())
    A = [list(input()) for _ in range(n)]
    B = [list(input()) for _ in range(m)]

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            swi = 1
            for k in range(m):
                if B[k] != A[i + k][j:j + m]:
                    swi = 0
                    break
            if swi == 1:
                print("Yes")
                return

    print("No")


if __name__ == '__main__':
    main()
