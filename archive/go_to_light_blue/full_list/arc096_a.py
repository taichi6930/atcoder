def main():
    a, b, c, x, y = map(int, input().split())
    print(min(a + b, c * 2) * min(x, y) + (x - min(x, y)) *
          min(a, c * 2) + (y - min(x, y)) * min(b, c * 2))


if __name__ == '__main__':
    main()
