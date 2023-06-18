def main():
    n = int(input())
    sList = [""] * n
    for i in range(n):
        sList[i] = input()
    print(len(set(sList)))


if __name__ == '__main__':
    main()
