def main():
    n = int(input())

    D = [1 for _ in range(n + 1)]

    for i in range(n - 1):
        D[i + 2] = D[i + 1] + D[i]
    print(D[-1])


if __name__ == '__main__':
    main()
