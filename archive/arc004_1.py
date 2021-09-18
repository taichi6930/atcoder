def main():
    n = int(input())
    ans = 0
    xy = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n - 1):
        x1, y1 = xy[i][0], xy[i][1]
        for j in range(i + 1, n):
            x2, y2 = xy[j][0], xy[j][1]
            ans = max(ans, ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    print(ans)


if __name__ == '__main__':
    main()
