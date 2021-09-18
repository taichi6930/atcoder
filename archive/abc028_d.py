def main():
    n, k = map(int, input().split())
    denominator = n ** 3
    numerator = 1 + (n - 1) * 3 + (k - 1) * (n - k) * 6

    print(numerator / denominator)


if __name__ == '__main__':
    main()
