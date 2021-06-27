import collections
import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    s = list(input())
    counter = collections.Counter(s)
    countermin = min(counter.values()) if len(counter.values()) == 3 else 0
    a, b, c = counter["a"] - countermin, counter["b"] - \
        countermin, counter["c"] - countermin
    print("YES" if max(a, b, c) <= 1 else "NO")


if __name__ == '__main__':
    main()
