def main():
    ans = 1
    n = int(input())

    for i in range(n):
        ans *= (i + 1)
    print(ans + 1)


if __name__ == '__main__':
    main()
