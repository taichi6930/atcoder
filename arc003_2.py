def main():
    n = int(input())
    S = [input()[::-1] for _ in range(n)]
    S.sort()

    for s in S:
        print(s[::-1])


if __name__ == '__main__':
    main()
