def main():
    n, w = map(int, input().split())
    ans = 0
    AB = sorted([list(map(int, input().split()))
                for _ in range(n)], reverse=True)
    for i in range(n):
        a, b = AB[i]
        c = min(b, w)
        ans += a * c
        w -= c
        if w <= 0:
            break
    print(ans)


if __name__ == '__main__':
    main()
