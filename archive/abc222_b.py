def main():
    n, p = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    ans = 0
    for a in A:
        if a < p:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
