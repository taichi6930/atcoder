def main():
    n = int(input())
    H = list(map(int, input().split()))

    ans = H[0] - 1

    for i in range(n):
        if H[i] <= ans:
            break
        ans = H[i]
    print(ans)


if __name__ == '__main__':
    main()
