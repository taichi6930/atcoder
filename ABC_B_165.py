def main():
    x = int(input())
    y = 100
    num = 0
    while 10 ** 18 >= y:
        y = int(y * 1.01)
        num += 1
        if x <= y:
            print(num)
            return


if __name__ == '__main__':
    main()
