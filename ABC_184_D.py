from collections import Counter


def main():
    a, b, c = map(int, input().split())
    print(((100 - a) * a + (100 - b) * b + (100 - c) * c)/(a + b + c))


if __name__ == '__main__':
    main()
