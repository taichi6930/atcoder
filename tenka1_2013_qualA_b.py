def main():
    n = int(input())
    ans = 0

    for i in range(n):
        ans += 1 if 20 > sum(list(map(int, input().split()))) else 0

    print(ans)


if __name__ == '__main__':
    main()
