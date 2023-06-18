def main():
    n, p = map(int, input().split())
    ans = int(p ** (1 / n))

    while ans > 0:
        a = ans ** n
        if p % a == 0:
            print(ans)
            return
        ans -= 1


if __name__ == '__main__':
    main()
