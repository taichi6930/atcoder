def main():
    a, b = map(int, input().split())
    print(b - a - (0 if a * b > 0 else 1))


if __name__ == '__main__':
    main()
