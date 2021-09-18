def main():
    a, b, c, d = map(int, input().split())
    print("Yes" if min(b, d) >= max(a, c) else "No")


if __name__ == '__main__':
    main()
