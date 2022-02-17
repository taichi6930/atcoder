def main():
    n = int(input())
    print(2 * n * (n + 1) - sum(list(map(int, input().split()))))


if __name__ == '__main__':
    main()
