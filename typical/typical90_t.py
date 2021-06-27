def main():
    a, b, c = map(int, input().split())
    print("Yes" if c ** b > a else "No")


if __name__ == '__main__':
    main()
