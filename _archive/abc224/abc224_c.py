def main():
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if XY[i][0] * (XY[j][1] - XY[k][1]) + XY[j][0] * (XY[k][1] - XY[i][1]) + XY[k][0] * (XY[i][1] - XY[j][1]) != 0:
                    ans += 1
    print(ans)


if __name__ == '__main__':
    main()
