def main():
    k, s = [input() for _ in range(2)]
    print(s[0:int(k)] + "..." if len(s) > int(k) else s)


if __name__ == '__main__':
    main()
