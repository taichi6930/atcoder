def main():
    n = int(input())
    ans = -1
    for i in range(n):
        a, p, x = map(int, input().split())
        if x - a > 0:
            if ans == -1:
                ans = p
                continue
            ans = min(ans, p)
    print(ans)


if __name__ == '__main__':
    main()
