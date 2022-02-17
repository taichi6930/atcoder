def main():
    n, k = map(int, input().split())
    T = [int(input()) for _ in range(n)]
    ans = -1

    for t in range(n - 2):
        if sum(T[t: t + 3]) < k:
            ans = t + 3
            break
    print(ans)


if __name__ == '__main__':
    main()
