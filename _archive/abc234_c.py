def main():
    k = int(input())
    bk = str(bin(k)).replace('0b', '').replace('1', '2')
    print(bk)


if __name__ == '__main__':
    main()
