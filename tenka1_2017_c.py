def main():
    n = int(input())
    for a in range(1, 3501):
        for b in range(1, 3501):
            q = 4 * a * b - n * (a + b)
            if q <= 0:
                continue
            if (n * a * b) % q == 0:
                print(a, b, (n * a * b) // q)
                return


if __name__ == '__main__':
    main()
