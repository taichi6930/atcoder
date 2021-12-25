def main():
    a, b = map(str, input().split())
    print("Yes" if a == b.upper() else "No")


if __name__ == '__main__':
    main()
