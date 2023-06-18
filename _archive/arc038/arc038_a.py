def main():
    n = int(input())
    print(sum(sorted(list(map(int, input().split())), reverse=True)[0::2]))


if __name__ == '__main__':
    main()
