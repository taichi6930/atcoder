def main():
    X = list(input())
    n = len(X)

    ans = 0

    for i in range(n):
        if X[i] == "S":
            ans = i * 2
            break

    for j in range(n):
        if X[n - 1 - j] == "T":
            ans = min(j * 2, ans)
            break

    print(ans)


if __name__ == '__main__':
    main()
