def main():
    k, a, b = map(int, input().split())

    if a >= b - 2 or a - 1 >= k:
        print(1 + k)
        return

    ans = 1
    ans += a - 1
    k -= a - 1
    ans += (k // 2) * (b - a) + k % 2
    print(ans)


if __name__ == '__main__':
    main()
