def main():
    n = int(input())
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        ans += a * b
    print(int(ans * 1.05))


if __name__ == '__main__':
    main()
