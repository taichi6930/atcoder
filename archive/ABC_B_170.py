def main():
    x, y = map(int,  input().split())
    c = y - 2 * x
    a = c % 2 == 0 and c >= 0 and y - 4 * x <= 0
    print('YNeos'[not(a)::2])


if __name__ == '__main__':
    main()
