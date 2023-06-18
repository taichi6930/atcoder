def main():
    a, b = map(int, input().split())
    print('Yes' if (b-a) == 1 or (max(a, b) == 10 and min(a, b) == 1) else 'No')


if __name__ == '__main__':
    main()
