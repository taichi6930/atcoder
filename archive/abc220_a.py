def main():
    a, b, c = map(int, input().split())
    d = b // c * c
    print(d if d >= a else -1)


if __name__ == '__main__':
    main()
