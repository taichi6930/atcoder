def main():
    h, w = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(h)]

    for i1 in range(h - 1):
        for j1 in range(w - 1):
            for i2 in range(i1 + 1, h):
                for j2 in range(j1 + 1, w):
                    if A[i1][j1] + A[i2][j2] > A[i1][j2] + A[i2][j1]:
                        print('No')
                        return
    print('Yes')


if __name__ == '__main__':
    main()
