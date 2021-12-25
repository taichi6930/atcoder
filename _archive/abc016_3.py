def main():
    n, m = map(int, input().split())
    K = [[]] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        if b in K[a]:
            return
        K[a] = K[a] + [b]
    print(K)


if __name__ == '__main__':
    main()
