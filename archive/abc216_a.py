def main():
    x, y = map(int, input().split("."))
    if y >= 0 and y <= 2:
        print(str(x) + '-')
        return
    if y >= 3 and y <= 6:
        print(str(x))
        return
    if y >= 7 and y <= 9:
        print(str(x) + '+')
        return


if __name__ == '__main__':
    main()
