def main():
    x, y = map(int, input().split())
    if y == 0:
        print('ERROR')
        return
    k = int(100 * x / y) / 100
    print('{:.2f}'.format(k))


if __name__ == '__main__':
    main()
