def main():
    n, D, H = map(int, input().split())
    ans = 0

    for _ in range(n):
        d, h = map(int, input().split())
        ans = max(ans, (h * D - H * d) / (D - d))

    print(ans)


if __name__ == '__main__':
    main()
