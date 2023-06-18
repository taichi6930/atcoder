def main():
    n, m = map(int, input().split())
    xy = sorted([list(map(int, input().split())) for _ in range(m)])
    A = [1] + [0] * (n - 1)
    swi = 0
    for i in range(m):
        x, y = xy[i][0], xy[i][1]
        if swi == 0:
            if x == 1:
                A[0] = 0
                A[y - 1] = 1
                swi = 1
                print(A)
                continue
        if A[x - 1] == 1:
            A[y - 1] = 1
            print(A)
    print(A)
    print(sum(A))


if __name__ == '__main__':
    main()
