import math


def main():
    n = int(input())
    for a in range(1, 100):
        if n <= 3 ** a:
            break
        for b in range(1, 100):
            if n < 3 ** a + 5 ** b:
                break
            if n == 3 ** a + 5 ** b:
                print(a, b)
                return
    print(-1)


if __name__ == '__main__':
    main()
