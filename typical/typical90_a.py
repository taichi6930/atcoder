def main():
    n, l = map(int, input().split())
    k = int(input())
    a = [0] + list(map(int, input().split())) + [l]
    b = [None] * (n + 1)

    for i in range(n + 1):
        b[i] = a[i + 1] - a[i]


if __name__ == '__main__':
    main()
