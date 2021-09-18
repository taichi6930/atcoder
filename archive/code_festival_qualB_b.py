
def main():
    n, k = map(int, input().split())
    cnt = 0
    ans = None

    for i in range(n):
        a = int(input())
        if not ans is None:
            continue

        cnt += a

        if cnt >= k:
            ans = i + 1

    print(ans)


if __name__ == '__main__':
    main()
