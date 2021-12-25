import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    print(sum([is_prime(i) for i in range(int(input()))]) - 1)


if __name__ == '__main__':
    main()
