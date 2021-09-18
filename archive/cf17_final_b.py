import collections


def main():
    s = list(input())
    counter = collections.Counter(s)
    countermin = min(counter.values()) if len(counter.values()) == 3 else 0
    a, b, c = counter["a"] - countermin, counter["b"] - \
        countermin, counter["c"] - countermin
    print("YES" if max(a, b, c) <= 1 else "NO")


if __name__ == '__main__':
    main()
