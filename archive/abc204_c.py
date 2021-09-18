def main():
    n, m = map(int, input().split())
    AtoB = [[]] + [[None]] * n
    for i in range(m):
        a, b = map(int, input().split())
        AtoB[a].append(b)
    print(AtoB)


if __name__ == '__main__':
    main()
