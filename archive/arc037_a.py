def main():
    n = int(input())
    print(sum([max(0, 80 - a) for a in list(map(int, input().split()))]))


if __name__ == '__main__':
    main()
