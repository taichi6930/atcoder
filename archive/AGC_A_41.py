def main():
    n, a, b = map(int,  input().split())
    if (b - a) % 2 == 0:
        print((b - a) // 2)
        return
    print(min(a-1, n-b) + (b - a + 1)//2)


if __name__ == '__main__':
    main()
