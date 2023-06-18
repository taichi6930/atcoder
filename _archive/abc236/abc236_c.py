def main():
    n, m = map(int, input().split())
    S = list(map(str, input().split()))
    T = list(map(str, input().split()))

    a = 0

    for s in S:
        if s != T[a]:
            print('No')
            continue
        print('Yes')
        a += 1


if __name__ == '__main__':
    main()
